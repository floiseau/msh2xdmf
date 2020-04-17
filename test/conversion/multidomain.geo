
// Parameters
a = DefineNumber[ 1.0, Name "Parameters/Lx" ];
d = DefineNumber[ 0.1, Name "Parameters/Density" ];

// Points
Point(1) = {0,  0, 0, d};
Point(2) = {a,  0, 0, d};

Point(3) = {a,  a, 0, d};
Point(4) = {0,  a, 0, d};

Point(5) = {a, -a, 0, d};
Point(6) = {0, -a, 0, d};

// Line
Line(1) = {1, 2};

Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Line(5) = {2, 5};
Line(6) = {5, 6};
Line(7) = {6, 1};

// Surfaces
Curve Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};
Curve Loop(2) = {1, 5, 6, 7};
Plane Surface(2) = {2};

// Mesh
Transfinite Surface {1};
Transfinite Surface {2};

// Domain
Physical Surface("top_domain") = {1};
Physical Surface("bot_domain") = {2};

// Boundaries
Physical Line("middle") = {1};
Physical Line("right") = {2, 5};
Physical Line("top") = {3};
Physical Line("bot") = {6};
Physical Line("left") = {4, 7};
