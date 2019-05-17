person(lisa, female, 180, 30, phd).
person(jenny, female, 167, 25, hs).
person(bob, male, 180, 40, phd).
person(charles, male, 190, 30, masters).
person(arnold, male, 177, 29, hs).

edu(phd, 4).
edu(masters, 3).
edu(bs, 2).
edu(btech, 2).
edu(ug, 2).
edu(college, 2).
edu(hs, 1).

edu_ge(X,Y):-edu(X,Z), edu(Y, Z1), Z>=Z1.
older(X,Y):- X>=Y.
dateable(Woman, Man):- person(Woman, female, H1, Age1, Edu1) , person(Man, male, H2, Age2, Edu2) , H2 >= H1, edu_ge(Edu2, Edu1), older(Age1+5, Age2).