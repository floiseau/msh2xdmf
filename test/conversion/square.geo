
// Parameters
a = DefineNumber[ 1.0, Name "Parameters/Lx" ];
d = DefineNumber[ 0.1, Name "Parameters/Density" ];

// Points
Point(1) = {0, 0, 0, d};
Point(2) = {a, 0, 0, d};
Point(3) = {a, a, 0, d};
Point(4) = {0, a, 0, d};

// Line
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

// Surfaces
Curve Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

// Mesh
Transfinite Surface {1};

// Domain
Physical Surface("domain") = {1};

// Boundaries
Physical Line("bot") = {1};
Physical Line("right") = {2};
Physical Line("top") = {3};
Physical Line("left") = {4};
