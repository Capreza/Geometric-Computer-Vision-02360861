Q1 - b
====================
As time increases the image becomes blurrer. this is due to a reduction in dirichlet energy.
in the original image we had sharp edges and fine details and as time progresses we can see we lose those until we reach mostly large blotches of white and black with some grayness on their borders.
If we would let the simulation run for a very long time we would reach a gray block in which each pixels value would be (sum of all initial pixel values ) / (numer of pixels)


Q1 - c
====================

Dirichlet: The edges are clearly stuck at initial values, looking unnatural in comparison to rest of image, and bleeding inward. As most of the border of the image is bright as time passes this image becomes the brightest by a significant difference.

Neumann: The edges look more natural and "insulated," as if the image just blurs within its own frame.

Periodic: Information from edges mixes creating blotches of color that wraparound the image, color is less focused here in relation to Neumann where the color spereates more neatly.

Q4 - 4
====================
As we can see in the attached visualization, the heat spreads out in space, 
causing the middle to become colder over time also the periphery follows a pattern - heat reaches it for the first time, heats up until a point, then starts getting colder as heat speards out even further.
also, the countour lines become more spread out over time, meaning there are larger areas that have the same heat (approximately) meaning we have an initial state 
of a very sharp peak which flattens out to a more moderate hill.
another interesting point to point out is that heat speards out faster earlier in the simulation (increase in radius of circles).

Q5 
====================
Similarities to Q4 (same paragraph)
-----------------
As we can see in the attached visualization, the heat spreads out in space, 
causing the middle to become colder over time also the periphery follows a pattern - heat reaches it for the first time, heats up until a point, then starts getting colder as heat speards out even further. 
also, the countour lines become more spread out over time, meaning there are larger areas that have the same heat (approximately) meaning we have an initial state 
of a very sharp peak which flattens out to a more moderate hill.

another interesting point to point out is that heat speards out faster earlier in the simulation (increase in radius of circles).

Difference from Q4
-----------------
The speard of heat is epliptical, this is due to heat spreading more in the main axis of the eplise, the eigenvalues of A used in this experiment (A=[[4,1],[1,2]]) are 4.41~ and 1.59~ which means the heat travels 3~ times as fast in the main axis than in the secondary one. (in the case of A=[2,0],[0,2]) we would get a circular spread since there would be no preferred axis)
Also, this causes heat to spread much faster in general when compared to the previous simulation with alpha = 0.5
