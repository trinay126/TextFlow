# pipeline.py
# the pipeline executor. Runs a list of stage functions in sequence
# Each stage takes a string and returns a transformed string,

def run_pipeline(text, stages):
    """
    Run a list of stage functions on tect in order

    Args :
        text : the input string to process
        stages : list of (stage_name, stage_funciton, Config_dict) tuples
    Returns :
        processed_text : the final string after all stages
        log : list of dicts describing what each stages did
    """
    current = text
    log = []

    for stage_name, stage_func, config in stages:
        before = len(current)
        current = stage_func(current, **config)
        after = len(current)

        log.append({
            "stage" : stage_name,
            "before": before,
            "after" : after,
            "removed" : before - after ,
         })
    return current, log

def build_stage(name, func, **config):
    """
    Helper to build a stage tuple cleanly

    Usage :
        build_stage("lowercase", to_lowercase)
        build_stage("stopwords", remove_stopwords, lang="en)
    """
    return (name, func, config)

def log summary
