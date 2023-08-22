import hydra
import mlflow
from hydra.core.hydra_config import HydraConfig
from hydra.utils import call, instantiate
from loguru import logger
from omegaconf import DictConfig, OmegaConf
from sklearn.pipeline import Pipeline

from auto_review.utils import (
    log_best_params,
    log_config,
    log_feature_importance,
    log_script,
    make_logfile,
)


@logger.catch
def run(cfg: DictConfig, outputs_dir: str) -> None:
    logger.info(OmegaConf.to_yaml(cfg))
    df = call(cfg.read)
    for t in cfg.get("transform", []):
        df = call(t, df=df)
    for f in cfg.get("feature", []):
        df[f._target_] = call(f, df=df)
    for m in cfg.get("model", []):
        mlflow.set_experiment(cfg.experiment_name)
        pipe = Pipeline([(c._target_, instantiate(c)) for c in cfg.model[m]])
        X_train, X_test, y_train, y_test = call(cfg.split, df=df)
        with mlflow.start_run(run_name=m):
            pipe = call(cfg.train, model=pipe, X=X_train, y=y_train)
            call(cfg.eval, model=pipe, X=X_test, y=y_test)
            log_best_params(pipe)
            log_feature_importance(pipe, X_train.columns, path=outputs_dir)
            log_script(outputs_dir)
            log_config(outputs_dir)
    call(cfg.get("write", None), df=df)
    logger.info("Complete")


@hydra.main(config_path="./", config_name="default", version_base="1.3")
def hydra_run(cfg: DictConfig) -> None:
    make_logfile(HydraConfig.get().runtime.output_dir, __file__)
    run(cfg, outputs_dir=HydraConfig.get().runtime.output_dir)


if __name__ == "__main__":
    hydra_run()
