from data_prepare import *


def preprocess():
    df_data = generate_CTGan()
    smk = SMOTETomek()
    dat = df_data.drop(columns=["target"])
    m_g_objects,m_g_targets=smk.fit_resample(dat, df_data["target"])

    return train_test_split(
        m_g_objects,
        m_g_targets,
        test_size=0.2,
        #shuffle=False,
        random_state=42,
    )