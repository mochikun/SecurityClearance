import math

class CalcSC:
    IR=[0,0,0]
    RED=[255,0,0]
    OR=[255,165,0]
    YE=[255,255,0]
    GR=[0,128,0]
    BL=[0,0,255]
    IN=[75,0,130]
    VI=[238,130,238]
    UV=[255,255,255]
    SC=[IR, RED, OR, YE, GR, BL, IN, VI, UV]

    def __init__(self, debug=False, min=0, max=40):
        self.DEBUG=debug
        self.MIN=min
        self.MAX=max

    def setVal(self, input):
        self.inval=float(input)
        self.dp(self.inval)

    def dp(self,msg): # Debug Print
        if self.DEBUG:
            print msg

    def calc_rgb(self, level, lowlv, rgb):
        return int(self.SC[int(level)][rgb] - lowlv*(self.SC[int(level)][rgb] - self.SC[int(level)+1][rgb]))

    def calc_bitrate(self, rgb):
        return int(math.fabs(100*(float(rgb)/255)))

    def return_rgb(self):
        if self.inval <= self.MIN:
            level =  0
            [r, g, b] = self.SC[level]
        elif self.inval >= self.MAX:
            level = 8
            [r, g, b] = self.SC[level]
        else:
            level = 8*(self.inval - self.MIN)/(self.MAX-self.MIN)
            lowlv = level - int(level)
            self.dp(lowlv)
            [r, g, b] = [self.calc_rgb(level, lowlv, x) for x in [0, 1, 2]]
        self.dp(level)
        self.dp([r,g,b])
        return [r, g, b]

    def return_rgbrate(self):
        [r, g, b] = self.return_rgb()
        [rp, gp, bp] = map(self.calc_bitrate, [r, g, b])
        self.dp([rp,gp,bp])
        return [rp, gp, bp]

if __name__ == "__main__":
    secc = CalcSC()
    secc.setVal(18.9)
    [r, g, b] = secc.return_rgb()
    [rp, gp, bp] = secc.return_rgbrate()
    print ([r,g,b])
    print ([rp,gp,bp])
