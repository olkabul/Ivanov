basic_formatting_expected = """cbing.txt Contact info: +1-789-456-123; cbing@mail.com. 5
jtribbiani.txt He is portrayed by Matt LeBlanc in both series (jtribbiani@friendsmail.fr). 2
mgeller.txt Created by David Crane and Marta Kauffman, and portrayed by actress Courteney Cox (+1-123-456-789, mgeller@friendsmail.frn), Monica appears in all of the show's 236 episodes, from its premiere in 1994, to its finale in 2004. 2
pbuffay.txt For her portrayal of Phoebe Buffay, Kudrow (contact info: pbuffay@friendsmail.frn) received a Primetime Emmy Award, a Screen Actors Guild Award, a Satellite Award, and an American Comedy Award, as well as a Golden Globe Award nomination. 2
rgeller.txt Ross Geller, Ph.D., portrayed by David Schwimmer (ross_geller@col-un.edu), is one of the six main fictional characters of the NBC sitcom Friends. 1
rgreen.txt Portrayed by Jennifer Aniston (contact rgreen@friendsmail.frn), the character was created by David Crane and Marta Kauffman, and appeared in all of the show's 236 episodes during its decade-long run, from its premiere on September 22, 1994 to its finale on May 6, 2004. 2
"""

under_formatting_expected = """cbing.txt Contact info: +1-789-456-123; cbing@mail.com. 5
                                       ^
jtribbiani.txt He is portrayed by Matt LeBlanc in both series (jtribbiani@friendsmail.fr). 2
                                                              ^
mgeller.txt Created by David Crane and Marta Kauffman, and portrayed by actress Courteney Cox (+1-123-456-789, mgeller@friendsmail.frn), Monica appears in all of the show's 236 episodes, from its premiere in 1994, to its finale in 2004. 2
                                                                                                              ^
pbuffay.txt For her portrayal of Phoebe Buffay, Kudrow (contact info: pbuffay@friendsmail.frn) received a Primetime Emmy Award, a Screen Actors Guild Award, a Satellite Award, and an American Comedy Award, as well as a Golden Globe Award nomination. 2
                                                                     ^
rgeller.txt Ross Geller, Ph.D., portrayed by David Schwimmer (ross_geller@col-un.edu), is one of the six main fictional characters of the NBC sitcom Friends. 1
                                                             ^
rgreen.txt Portrayed by Jennifer Aniston (contact rgreen@friendsmail.frn), the character was created by David Crane and Marta Kauffman, and appeared in all of the show's 236 episodes during its decade-long run, from its premiere on September 22, 1994 to its finale on May 6, 2004. 2
                                                 ^
"""

machine_formatting_expected = """cbing.txt:5:30:cbing@mail.com
jtribbiani.txt:2:48:jtribbiani@friendsmail.fr
mgeller.txt:2:99:mgeller@friendsmail.frn
pbuffay.txt:2:58:pbuffay@friendsmail.frn
rgeller.txt:1:50:ross_geller@col-un.edu
rgreen.txt:2:39:rgreen@friendsmail.frn
"""