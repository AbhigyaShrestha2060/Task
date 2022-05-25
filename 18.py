a=[2,34,56,78,75,78,69]
b=set(a)
b.remove(max(b))
b.remove(max(b))
a=list(b)
print(max(a),type(a))