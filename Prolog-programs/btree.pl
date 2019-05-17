nodes([] , 0).
emptytree([], []).

nonempty([Root, Lchild, Rchild]):- Root>0; nonempty(Lchild); nonempty(Rchild).

btree([]).
btree([Root, Lchild, Rchild]):-Root>=0 , btree(Lchild) , btree(Rchild).

node([], 0).
node([_, Left, Right], N):-node(Left,N1),node(Right,N2), N is N1+N2+1.

isempty([]).
isempty([Root, Left, Right]):-Root\=0, isempty(Left),isempty(Right).

check([],[]).
check([Root1, Left1, Right1], [Root2, Left2, Right2]):-balanced(Left1, Right1), balanced(Left2, Right2).

full([]).
full([Root, Left, Right]):-Root>0, check(Left, Right).
