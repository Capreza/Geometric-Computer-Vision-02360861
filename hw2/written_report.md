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