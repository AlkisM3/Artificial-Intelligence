directed_by(X,Y) :- findall(M,director(M,X),Y).

very_common(X,Y):-
 genre(X,G1), 
 genre(Y,G1),
 genre(X,G2), 
 genre(Y,G2),
 genre(X,G3), 
 genre(Y,G3),
 G1 \= G2,
 G1 \= G3,
 G2 \= G3,
 X \= Y. 

common(X,Y):-
 genre(X,G1), 
 genre(Y,G1),
 genre(X,G2), 
 genre(Y,G2),
 G1 \= G2,
 X \= Y.

not_common(X,Y):-
  not(very_common),
  not(common),
  X \= Y.

common_director(X,Y):-
  director(X,D),
  director(Y,D),
  X \= Y.

same_plot(X,Y):-
 plot_key(X,P1), 
 plot_key(Y,P1),
 plot_key(X,P2), 
 plot_key(Y,P2),
 plot_key(X,P3), 
 plot_key(Y,P3),
 P1 \= P2,
 P1 \= P3,
 P2 \= P3,
 X \= Y. 

common_plot(X,Y):-
 plot_key(X,P1), 
 plot_key(Y,P1),
 plot_key(X,P2),
 plot_key(Y,P2),
 P1 \= P2,
 X \= Y.

all_actors(X,Y):-
  actor(X,A1),
  actor(Y,A1),
  actor(X,A2),
  actor(Y,A2),
  actor(X,A3),
  actor(Y,A3),
  A1 \= A2,
  A1 \= A3,
  A2 \= A3,
  X \= Y.

many_actors(X,Y):-
 actor(X,A1),
 actor(Y,A1),
 actor(X,A2),
 actor(Y,A2),
 A1 \= A2,
 X \= Y.

some_actors(X,Y):-
  actor(X,A1),
  actor(Y,A1),
  X \= Y.

same_language(X,Y):-
  language(X,L),
  language(Y,L),
  X \= Y.

popular(X):-
 popularity(X,P),
 atom_number(P,N),
 N > 10000000000.

good_movie(X):-
 vote_average(X,V),
 atom_number(V,N),
 N > 7.

great_movie(X):-
  vote_average(X,V),
  atom_number(V,N),
  N > 8.


common_color(X,Y):-
  plot_key(X,'black and white'),
  plot_key(Y,'black and white'),
  X \= Y.

common_color(X,Y):- 
 with_color(X),
 with_color(Y),
 X \= Y.

greater_duration(X,Y):-
 duration(X,D1),
 duration(Y,D2),
 atom_number(D1,N1),
 atom_number(D2,N2),
 N2 >= N1,
 X \= Y.