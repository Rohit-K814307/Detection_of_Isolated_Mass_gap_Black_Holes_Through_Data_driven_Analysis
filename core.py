from data_preprocess import *

class BhData(Dataset):
    
    def __init__(self,m_g_objects,m_g_targets):
        x = m_g_objects.values
        y = m_g_targets.values
    
        self.x_train=torch.tensor(x,dtype=torch.float32)
        self.y_train=torch.tensor(y,dtype=torch.float32)
    
    def __len__(self):
        return len(self.y_train)
    
    def __getitem__(self,idx):
        return self.x_train[idx],self.y_train[idx]

def initialize_data():

    x_train, x_test, y_train, y_test = preprocess()

    X_train = torch.tensor(x_train.values)
    Y_train = torch.tensor(y_train.values)
    X_test = torch.tensor(x_test.values)
    Y_test = torch.tensor(y_test.values)

    bh_ns = BhData(x_train,y_train)
    train_loader = DataLoader(bh_ns,batch_size=10,shuffle=False)

    bh_ns_two = BhData(x_test, y_test)
    test_loader = DataLoader(bh_ns_two)


    return X_train, Y_train, X_test, Y_test, train_loader, test_loader


def create_models():
    