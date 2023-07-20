from models import *


def train_DBN(X_train, Y_train):

    dbn_bhns = DBN(visible_units=10 ,
            hidden_units=[23*23 ,1*1] ,
            k = 5,
            learning_rate = 0.01,
            learning_rate_decay = True,
            xavier_init = True,
            increase_to_cd_k = False,
            use_gpu = False
        )

    dbn_bhns.train_static(X_train, Y_train, 20, batch_size=10)




def train_RBF(train_loader, x_train):
    layer_widths = [10, 1]
    layer_centres = [40]
    basis_func = gaussian

    rbfnet = RadialBasisNet(layer_widths, layer_centres, basis_func)
    rbfnet.fit(train_loader, x_train, 500, 0.01, nn.BCEWithLogitsLoss())



def train_MLP(train_loader):
    model = mpnet()
    epochs = 100
    loss_fn = nn.BCELoss()
    learning_rate = 0.001
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    epoch = 0
    while epoch < epochs:
        epoch += 1
        batches = 0
        progress = 0
        for x_batch, y_batch in train_loader:
            batches += 1
            optimizer.zero_grad()

            y_pred = model(x_batch)
            y_batch = y_batch.unsqueeze(1)
            loss = loss_fn(y_pred, y_batch)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            progress += y_batch.size(0)

            if progress % 15 == 0:
                sys.stdout.write('\rEpoch: %d, Progress: %d, Loss: %f      ' % 
                                    (epoch, progress, loss))
                sys.stdout.flush()