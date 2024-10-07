# Elliptic curve and number of point on the curve

E= EllipticCurve(GF(97),[41,12])
print(E)
print("Number of points in the curve:",E.order())
print("Points in the elliptic curve:",E.points())