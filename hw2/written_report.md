Q1 
====================
C(p) is defined piece wise, so lets calculate C`(p) piecewise:

$$C'(p) = \begin{cases}
(1, 0, \frac{2}{p^3}e^{-1/p^2}) & \text{if } p > 0 \\
(1, \frac{2}{p^3}e^{-1/p^2}, 0) & \text{if } p < 0
\end{cases}$$
in order to show the C(p) is regular, we must show that for every p

$$C'(p) != 0$$

this is trivial for all p != 0 according to our previous derivation

for p=0 lets explain why this is also the case - 
to prove that the derivative exists in this point, well show that the right hand derivative exists and so does the left hand derivative and that they are the same:

for the right hand side (left is almost the same process):
$$\lim_{h \to 0^+} \frac{C(h) - C(0)}{h} = \lim_{h \to 0^+} \left( 1, 0, \frac{e^{-1/h^2}}{h} \right) = (1,0,0)$$

as this is not a calculus course i wont elaborate on why the third element`s limit is 0

left hand derivative is the same and so 

$$C'(p) = \begin{cases}
(1, 0, \frac{2}{p^3}e^{-1/p^2}) & \text{if } p > 0 \\
(1, \frac{2}{p^3}e^{-1/p^2}, 0) & \text{if } p < 0 \\ 
(1, 0, 0) & \text{if } p = 0
\end{cases}$$

so, C`(p) exists for all p and is different from (0,0,0) for all p 
-> C(p) is regular for all p

now lets show that:
kappa(p) != 0 for p!= 0, +- (2/3)**(1/2) 
and
kappa(0) = 0 

in order to calculate kappa we need to derive C`(p) to get C``(p):

(p=0 case is almost exactly the same as in previous part)

$$C''(p) = \begin{cases}
(0, 0, e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4})) & \text{if } p > 0 \\
(0, e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4}), 0) & \text{if } p < 0 \\ 
(0, 0, 0) & \text{if } p = 0
\end{cases}$$

$$\kappa(p) = \frac{||C'(p) \times C''(p)||}{||C'(p)||^3}$$

for the p>0 part (p<0 is almost the same)

$$\vec{C'(p)} \times \vec{C''(p)} = \det \begin{bmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 0 & \frac{2}{p^3}e^{-1/p^2}) \\
0 & 0 & e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4})
\end{bmatrix}$$

$$C' \times C'' = (0, -e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4}), 0)$$

the result in the p< 0 case is 

$$C' \times C'' = (0, 0, e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4}))$$

in both cases 

$$||C'(p) \times C''(p)|| = \sqrt{((e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4}))^2} =  |e^{-1/p^2}*(\frac{4}{p^6} - \frac{6}{p^4})|$$

similarly, in both regions
$$||C'(p)|| =  \sqrt{1 + (\frac{2}{p^3}e^{-1/p^2})^2} $$
$$||C'(p)||^3 =  (\sqrt{1 + (\frac{2}{p^3}e^{-1/p^2})^2})^3 $$

lets show where kappa = 0
assuming the denominator ( which is the case for all p!=0 where it is defined, as it is 1+something squared, therefore >=1 ) is not 0, kappa will be 0 where the numerator is 0
so we are looking for 

$$e^{-1/p^2}\left(\frac{4}{p^6} - \frac{6}{p^4}\right) = 0$$

because the exponent is never 0 we are looking for
$$\left(\frac{4}{p^6} - \frac{6}{p^4}\right) = 0$$
$$\frac{4}{p^6}  =  \frac{6}{p^4}$$
$$4  =  6p^2$$
$$\frac{2}{3}  =  p^2$$
$$ p = +- \sqrt{\frac{2}{3}}$$

so indeed for  these values: 
$$ kappa = 0 $$
and for all other values of p!= 0 kappa !=0

now lets address p=0

$$\kappa(0) = \frac{||C'(0) \times C''(0)||}{||C'(0)||^3}$$
$$\kappa(0) = \frac{||(1,0,0) \times (0,0,0)||}{||(1,0,0)||^3}$$
$$\kappa(0) = \frac{0}{1} = 0$$




Q5 - Evaluation - 5 
====================
The Cartan`s signature curve of the original curve and the euclidian transformed curve are the same, showing kappa and kappa_s are invariants under this group of transformations.
This is because the arc length and local bend of the curve did not change following the euclidian transformation.
However, the equi-affine transformation changed the Cartan`s signature curve drastically, besides changing the shape slightly, it changed the magnitude significantly - notice the y axis in the original curve going between -30 and 30 and after the transformation it turns into -200,200.
This is because the arc length and local bend change.
We expect that if we would have used an affine invariant calculation of arc length that the three signature curves would be the same.

Q5 - Additional Questions - 1 
====================
Removing a section of one of the curves will remove a corresponding section from the resulting signature curve.
So, if we take two curves, one of which is euclidian transformation of the other, remove a part of one of them and then compare the signature curves,
for each point in the resulting signature curve of the occluded curve we should find a corresponding point in the non-occluded curve.
and if the transformation is equi-affine we still wouldnt be able to match them because the occlusion did not change remaining part of the occluded signature curve.

Q5 - Additional Questions - 2 
====================
The problem - a non convex curve implies the existence of points where curvature = 0, these are points where the curve changes from bending inward to outward.
If we are using Euclidean invariants as we have in this exercise having such points make the signature graph jagged and erratic,
this is because near these points of curve = 0 the gradients and division are unstable, since small numerical changes due to numerical sampling become very pronounced, this is especially true for the equi-affine transformed curve.

We should also point out that if we would have used an affine invariant curve length, since calculating curvature involves dividing by distance, and the distance is proportional to curvature, in the curvature ~= 0 points we would get division by zero - or more probably division by something that is very close to 0, resulting in nan


Q7 - Neural Geometry Processing via Spherical Neural Surfaces
====================
The paper introduces a new type of representation of genus-0 surfaces (objects without a hole in them).
This new representation is created by overfitting a neural network trained to map coordinates of a sphere to coordinates of corresponding points in the surface it is trying to represent.
________
While neural network representations of surfaces were not a new idea, this new representation is unique in the fact that it allows direct mathematical operations (such as calculating the Laplace Beltrami operator, calculating First/Second Fundemental forms, etc...) done on the explicit representation of the surface, as opposed to many other neural representations which up till this point did this by creating a mesh from samples generated from the implicit representation of the surface the nerual network learned, and operating in the standard discrete way to calculate these.
________
Given the trained network, the researches could calculate various properties of the represented surface using various tools like autograd. A built in feature to most modern ML framworks allowing users to easily calculate derivatives.
Using this it was trivial to calculate a derivative at any point in the represented surface.
________
In order to create this overfitting network, the researchers used a standard mlp, which received a 3 coordinate vector which represented the source point in the unit sphere and output a 3 coordinate vector which represented the destination point in the target surface. 
As a loss function they used the distance between output coordinates and ground truth coordinates and added a regularization term which penalized a results in which the normal vector calculated using the neural network and the normal vector calculated using the ground truth diverged.
________

The results of comparing the SNS representation to other methods (Monge-fitting, NFGP.i3D) were:
* Given a fine or medium resolution mesh, SNS (Almost) always was best at calculating postion,normals and curvature, this is not only impressive due to beating the perfomance of other methods, but also because it was able to do so with limited geometric data.
* SNS was fairly consistent at representing the same underlying surface given different meshes of the same as inputs.
 * SNS was the best method to approximate the surface LBO in analytical surfaces, and it was more consistent than mesh based LBOs when fitted to different meshes of the same surface.

Another noteworthy result was that the researchers were able to use the SNS and its derived properties (LBO, First Fundamental Form) to perform spectral analysis by training a separate neural network. The SNS geometry defined the loss function (Rayleigh Quotient) for this training.

________

 The drawbacks of this paper are:
 * It is very slow in comparison to other methods.
 * It is only relevant for genus-0 surfaces.
 * While the paper claims this method would work other inputs besides sampling from   meshes and analytical representations, it does not test or compare them extensivley.