from omegaconf import OmegaConf


def get_cfg(args):
    cfg = OmegaConf.load(args.cfg_path)

    structured_cfg = OmegaConf.structured(cfg)
    return structured_cfg
