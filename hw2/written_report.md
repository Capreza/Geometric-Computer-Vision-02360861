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