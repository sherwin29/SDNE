import itertools

class Config(object):
    def __init__(self):
        ## graph data
        #self.file_path = "../Data_SDNE/Flickr2_1.txt"
        self.file_path = "GraphData/blogCatalog3.txt"
        #self.label_file_path = "GraphData/blogCatalog3-groups.txt"
        ## embedding data
        self.embedding_filename = "embeddingResult/blog_100d/blog" 


        ## hyperparameter
        self.struct = [None, 1000, 100]
        ## the loss func is  // gamma * L1 + alpha * L2 + reg * regularTerm // 
        self.alpha = 500
        self.gamma = 1
        self.reg = 1
        ## the weight balanced value to reconstruct non-zero element more.
        self.beta = 10
        
        ## para for training
        #self.rN = 0.9
        self.batch_size = 64
        self.epochs_limit = 3
        self.learning_rate = 0.01
        self.display = 1

        self.DBN_init = True
        self.dbn_epochs = 500
        self.dbn_batch_size = 64
        self.dbn_learning_rate = 0.1

        self.sparse_dot = False
        # self.ng_sample_ratio = 0.0 # negative sample ratio
        self.ng_sample_num = 5
        
        #self.sample_ratio = 1
        #self.sample_method = "node"

    
    def combination(self):
        struct_mids = [600, 800, 1000]

        alphas = [200, 300, 500]
        regs = [1]
        betas = [10, 20, 30]

        learning_rates = [0.01]

        dbn_epochss = [500, 800, 100]
        dbn_learning_rates = [0.1]

        for comb in itertools.product(struct_mids, alphas, regs, betas, learning_rates, dbn_epochss, dbn_learning_rates):
            self.struct[1] = comb[0]
            self.alpha = comb[1]
            self.reg = comb[2]
            self.beta = comb[3]
            self.learning_rate = comb[4]
            self.dbn_epochs = comb[5]
            self.dbn_learning_rate = comb[6]
            yield self    

            
if __name__ == "__main__":
    for config in Config().combination():
        print config.alpha