import IntersectPoint as IPt
import Exceptions as exc

# ---------------1-------------
# обычный тест
#x + y = 1   - уравнение 1
#x + 2y = -2  - уравнение 2
#x = 4, y = -3    - точка пересечения

# ---------------2-------------
# обычный тест
#2x + 3y = 1  - уравнение 1
#x-y = -2     - уравнение 2
#x = -1, y = 1    - точка пересечения

# ---------------3-------------
# отрицательные и дробные коэффициенты
#-2.3x + 1.6y = 1.4  - уравнение 1
#6.4x + 9.7y = 19.1     - уравнение 2
#x = 0,5216589861, y = 1.624884792    - точка пересечения

# ---------------4-------------
#Прямые лежат на одной прямой
#x + y = 1  - уравнение 1
#x + y = 1     - уравнение 2
#Прямые совпадают


# ---------------5-------------
#Прямые параллельны и не пересекаются
#x + y = 1  - уравнение 1
#x + y = 2     - уравнение 2
#Прямые параллельны

Tests = [
    {
        'line1': [1,1,1], 'line2': [1,2,-2], 'ans':IPt.Point(4, -3),
    },
    {
        'line1': [2,3,1], 'line2': [1,-1,-2], 'ans':IPt.Point(-1,1),
    },
    {
        'line1': [-2.3,1.6,1.4], 'line2': [6.4,9.7,19.1], 'ans':IPt.Point(0.5216589861, 1.624884792),
    },
    {
        'line1': [1,1,1], 'line2': [1,1,1], 'ans':exc.StraightIsEqualError(),
    },
    {
        'line1': [1,1,1], 'line2': [1,1,2], 'ans':exc.StraightIsParallelError(),
    },
]


def TestIntersect(test):
    print("_____________Тест__________________")
    tline1 = test['line1']
    line1 = IPt.Line(tline1[0], tline1[1], tline1[2])

    tline2 = test['line2']
    line2 = IPt.Line(tline2[0], tline2[1], tline2[2])

    intersect = IPt.Intersect(line1, line2)

    try:
        res = intersect.find_cross()
    except Exception as e:
        res = e

    if(res.__str__() == test['ans'].__str__()):
        print(" Ok ")
    else:
        print(" Failed ")

    print("Первое уравнение {0}x + {1}y = {2}".format(line1.a,line1.b,line1.c))
    print("Второе уравнение {0}x + {1}y = {2}".format(line2.a,line2.b,line2.c))
      print("проверка уравнения 1 {0}x + {1}y = {2}".format(line2.a,line2.b,line2.c))
          print("проверка уравнения 2 {0}x + {1}y = {2}".format(line2.a,line2.b,line2.c))
    print("Полученный ответ {0}".format(res))
    print("Правильный ответ {0}".format(test['ans']))

def TestsIntersect():
    for test in Tests:
        TestIntersect(test)

TestsIntersect()

#print(testLines)
#print(testLines[0]['ans'])
#line1 = IPt.Line(a,b,c)
#line2 = IPt.Line(a,b,c)
#intersect = IPt.Intersect(line1, line2)
#self.frame_res.lbl['text'] = intersect.find_cross()


