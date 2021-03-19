s = '''i.like.this.program.very.much
pqr.mno'''
r = s.split(".")
d = r[::-1]
p = ".".join(d)
print(p)
