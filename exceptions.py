x = input("Enter a number")
y = input("Enter a number")

try:
    z = x/int(y)

except Exception as e:
    print("exceptoin occured",type(e).__name__)
    z = None
except Exception as e:
    print("exceptoin type",type(e).__name__)
    z = None

print(z)
