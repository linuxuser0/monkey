import os
import shutil
import glimpse.experiment
import glimpse.models

class CellHelper():
    
    def __init__(self, path, count, corpus, add_count=1, init_count=2): 
        self.path = path
        self.count = count # number of S2s
        self.exp = glimpse.experiment.ExperimentData()
        self.image_path = corpus.imagedir
        self.corpus = corpus
        self.corpus_path = os.path.join(self.path, "cell")
        self.exp.extractor.model = glimpse.models.MakeModel()
        print self.corpus

    def imprint(self):
        glimpse.experiment.SetCorpus(self.exp, self.corpus) 
        glimpse.experiment.MakePrototypes(self.exp, num_prototypes=self.count, algorithm="imprint")
        return [glimpse.experiment.GetPrototype(self.exp, n) for n in range(
            glimpse.experiment.GetNumPrototypes(self.exp))]

    def get_next_images(self):
        self.reset_cell()
        self.populate_cell()
        self.categorize_images()
        while not self.cell_check():
            self.add_images()
            self.categorize_images()

    def reset_cell(self):
        try:
            shutil.rmtree(self.celldir)
        except Exception:
            pass 

        try:
            os.makedirs(self.celldir)
            for s in self.corpus.subdirs:
                path = os.path.join(self.celldir, s) os.makedirs(path)

        except Exception:
            print "Could not create folder"

    def cell_check(self):
        try:
            for s in self.corpus.subdirs:
                if os.listdir(os.path.join(self.corpus_path, s)) < self.img_count:
                    return False
        except Exception:
            # What a failure.
            return False 

        return True

    def populate_cell(self):
       self.add_images(self.init_count) 
        
    def categorize_images(self):
        self.setup_temp()
        categories = get_categories()
        for s in self.corpus.subdirs:
            folder = os.path.join(self.corpus_path, s)
            for image in os.listdir(folder):
                fullpath = os.path.join(folder, image)
                category = categories[image] 
                target = os.path.join(self.temp_path, category)
                shutil.copy(fullpath, target)

        self.reset_cell()

        for s in self.corpus.subdirs:
            folder = os.path.join(self.temp_path, s)
            for image in os.listdir(folder):
                fullpath = os.path.join(folder, image)
                target = os.path.join(self.celldir, s)
                shutil.copy(fullpath, target)

    def add_images(self, count=self.add_count): 
        for n in xrange(count):
            name = random.choice(self.corpus.subdirs)
            folder = os.path.join(corpus.imagedir, name)
            item = random.choice(os.listdir(folder)) # MAKE UNUSED
            fullpath = os.path.join(folder, item)
            target = os.path.join(self.corpus, name)
            shutil.copy(fullpath, target)
