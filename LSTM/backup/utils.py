class EarlyStopping():
    """
    This is taken from page 199 of book. Idea is to show False as soon as new loss
    is bigger than previous loss
    Class creates an object that tracks the loss of an optimization procedure.
    self._loss ... the lowest loss value observed until a certain point
    self.patience ... the number of steps the validate method should continue
                      to return true despite giving a loss that is bigger than
                      previous losses
    """
    def __init__(self, patience=0, verbose=0):
        """
        
        The patience argument 
        """
        self._step = 0
        self._loss = float('inf')
        self.patience = patience
        self.verbose = verbose
        
    def validate(self, loss):
        """
        updates a loss and compares it with the smallest previous loss.
        """
        if self._loss < loss:
            self._step += 1
            if self._step > self.patience:
                if self.verbose:
                    print('early stopping')
                return True
        else:
            self._step = 0
            self._loss = loss
        return False
