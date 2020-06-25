class Licznik:
    def __init__(self, sex, age, weight, height, metabolism, food, drinkingTime, drinks):
        self.interval = 0.25
        # 15 minutes
        self.sex = sex
        self.age = age
        self.weight = weight
        self.height = height
        self.metabolism = {
            # for male: 0.13 - 0.17
            0: 0.13 + metabolism/100,
            # for female: 0.15 - 0.19
            1: 0.15 + metabolism/100
            # multiplied by 10 cuz of EBAC equation
        }
        self.delayByFood = {
            0: 0.25,
            1: 0.5,
            2: 0.75,
            3: 1
        }
        self.timeOfAbsorbtion = drinkingTime + self.delayByFood[food]
        self.alcoholAmount = self.calculateAlcoholMass(drinks)

    def totalBodyWater(self):
        if self.sex == 0: # male
            return 2.447 - (0.09156 * self.age) + (0.1074 * self.height) + (0.3362 * self.weight)
        else: # female
            return -2.097 + (0.1069 * self.height) + (0.2466 * self.weight)

    def calculateAlcoholMass(self, drinks):
        sum = 0
        for drink in drinks:
            sum += drink[1] * drink[0] * 0.79 / 100
            # 0.79 is density of ethanol
        return sum

    def permilesOfAlcoholPerQuarter(self):
        totalAlc = (0.806 * self.alcoholAmount * 1.2) / self.totalBodyWater()
        # 0.806 body water in blood
        return totalAlc * self.interval / self.timeOfAbsorbtion

    def calculate(self):
        T = 0
        nOfQuarters = self.timeOfAbsorbtion / self.interval
        alcPerQuarter = self.permilesOfAlcoholPerQuarter()
        burnPerQuarter = self.metabolism[self.sex] * self.interval
        EBAC = [0.001]
        time = [0]
        # human body gets rid of the whole alcohol after 21 days, so it never gets rid of it
        # helps to imitate do{}while() function too
        while EBAC[T] > 0:
            if T < nOfQuarters:
                EBAC.append(EBAC[T] + alcPerQuarter - burnPerQuarter)
                time.append(time[T] + self.interval)
                print(T*self.interval, "\t: pije\t\t", EBAC[T])
            else:
                EBAC.append(EBAC[T] - burnPerQuarter)
                time.append(time[T] + self.interval)
                print(T*self.interval, "\t: tzrezwieje ", EBAC[T])
            T += 1

        if EBAC[-1] < 0:
            EBAC[-1] = 0.0

        return [EBAC, time]
