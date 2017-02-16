

class HashNode:
    def __init__(self, nyckel, data):
        self.nyckel = nyckel
        self.data = data

    def __str__(self):
        return ("Artist: " +self.nyckel + "\nLåt: " + self.data[2])

class HashTabell:
    def __init__(self,size):
        self.size=size*2        
        self.hashlista=[None]*self.size

    def store(self, node):
        hashvärde = self.hash2(node.nyckel)
        hashIndex = hashvärde%self.size

        krock = True
        i = 1
        while krock:
            if hashIndex > self.size:
                hashIndex = hashIndex%self.size
            if self.hashlista[hashIndex] == None:
                self.hashlista[hashIndex] = node
                krock = False
            else:
                hashIndex = hashIndex + i*i
                i = i+1

    def search(self, nyckel):
    
        hashvärde = self.hash2(nyckel)
        hashIndex = hashvärde%self.size

        check = True
        i = 1
        while check:
            if hashIndex > self.size:
                hashIndex = hashIndex%self.size
                
            if self.hashlista[hashIndex] == None:
                raise KeyError
            elif nyckel == self.hashlista[hashIndex].nyckel:
                check = False
                return (self.hashlista[hashIndex])
            else:
                hashIndex = hashIndex + i*i
                i = i+1

    def hash2(self, s):
        #Tagen från förläsning
        result = 0            
        for c in s:                    
            result = result*32 + ord(c) 
        return result


def fileRead():
    d = HashTabell(10000000)
    with open("unique_tracks.txt", "r", encoding = "utf-8") as fil:
        for rad in fil:
            rad.strip('\n')
            låten = rad.split('<SEP>')

            
            
            songNode = HashNode(låten[2].lower(), [låten[1],låten[0],låten[3]])
            d.store(songNode)
    print(d.search('iron maiden'))
    print(d.search('texta'))
    print(d.search('dsageagoisdowad'))

fileRead()

#Clas Blank Julia Liu
