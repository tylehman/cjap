# Data frame append column funtion
import pandas as pd

def dfapp(comp_name, job_title, job_link, job_addr, job_posted, job_srch):
    df = pd.DataFrame()
    app = df.append({
                    'comp_name': comp_name,
                    'job_title': job_title,
                    'job_link': job_link,
                    'job_addr': job_addr,
                    'job_posted': job_posted,
                    'job_srch': job_srch
                    }, ignore_index=True)
    return app;
