import numpy as np
from tensorflow.keras.models import load_model

id_key = {
    "TouchPose_crossSession" : "session_id",
    "TouchPose_crossSubjects" : "subject_id",
    "TouchPose_crossGestures" : "gesture_id"
}

def get_data_splits(df, id_arr):
    X_cap, Y_depth = None, None
    for p_id in id_arr:
        df_extract = df.get_group(p_id)
        x_cap_img = np.array(df_extract["cap_img"].tolist())
        y_depth_img = np.array(df_extract["depth_img"].tolist())

        x_cap_img[x_cap_img < 0] = 0
        maxVal = 1400
        x_cap_img = x_cap_img/maxVal
        y_depth_img = y_depth_img/255

        if X_cap is None:
            X_cap = x_cap_img
            Y_depth = y_depth_img
        else:
            X_cap = np.vstack((X_cap, x_cap_img))
            Y_depth = np.vstack((Y_depth, y_depth_img))
    return X_cap, Y_depth

def get_model(identifier, model_path, test_set):
    if isinstance(test_set[0], str):
        model = load_model(model_path+"/"+identifier+"/"+test_set[0]+".hdf5")
    else:
        model = load_model(model_path+"/"+identifier+"/"+str(int(test_set[0]))+".hdf5")
    return model
