# Illustrations « dessinées » du site Jean Ferret Paysage (style plat, palette Forêt, arbre du logo B).
# python3 gen.py out/  -> un .svg par illustration
import math, os, sys

MAIN, DK, ACC, LEAF = "#1f4d2e", "#163a22", "#7fae3e", "#a9cf6f"
SKY, HILL, GRASS, GRASS2 = "#eaf1e4", "#d3e3c0", "#8dbb4c", "#7fae3e"
WOOD, WOOD2, SOIL, SOIL2 = "#a8835c", "#8a6a48", "#b59572", "#9c7d5c"
SKIN, WHITE, GREY = "#e2b48c", "#ffffff", "#c9d2c6"
BGT, HEDGE, HEDGE2 = "#5e8c50", "#4f8a3a", "#3f7330"

def f(v): return f"{v:.1f}"

def oak(cx, cy, k, crown=ACC, trunk=WOOD2, leaf=LEAF, trunk_len=200, cut=None):
    """Arbre du logo B. cx, cy = centre de la couronne. cut = liste d'indices de cercles à retirer."""
    circles = [(0, -40, 92), (-78, 10, 70), (78, 10, 70), (-40, 50, 66), (40, 50, 66), (0, 30, 80)]
    if cut: circles = [c for i, c in enumerate(circles) if i not in cut]
    cr = "".join(f'<circle cx="{f(cx+x*k)}" cy="{f(cy+y*k)}" r="{f(r*k)}"/>' for x, y, r in circles)
    L = trunk_len
    t = (f'<path fill="{trunk}" d="M{f(cx-16*k)} {f(cy+L*k)} L{f(cx-10*k)} {f(cy+90*k)} '
         f'L{f(cx-52*k)} {f(cy+52*k)} L{f(cx-44*k)} {f(cy+44*k)} L{f(cx-6*k)} {f(cy+72*k)} '
         f'L{f(cx-4*k)} {f(cy+20*k)} L{f(cx+6*k)} {f(cy+20*k)} L{f(cx+6*k)} {f(cy+62*k)} '
         f'L{f(cx+44*k)} {f(cy+34*k)} L{f(cx+52*k)} {f(cy+42*k)} L{f(cx+12*k)} {f(cy+86*k)} '
         f'L{f(cx+16*k)} {f(cy+L*k)} Z"/>')
    lv = "".join(f'<ellipse cx="{f(cx+x*k)}" cy="{f(cy+y*k)}" rx="{f(14*k)}" ry="{f(7*k)}" transform="rotate({a} {f(cx+x*k)} {f(cy+y*k)})"/>'
                 for x, y, a in [(-50, -40, -30), (30, -80, 25), (70, -10, -20), (-90, 20, 35), (10, -10, 10), (-20, 60, -25), (60, 60, 30)])
    return f'{t}<g fill="{crown}">{cr}</g><g fill="{leaf}" opacity=".9">{lv}</g>'

def round_tree(cx, base, h, w, fill=BGT, trunk=WOOD2):
    """Petit arbre de fond : tronc + couronne ovale."""
    return (f'<rect x="{f(cx-w*.06)}" y="{f(base-h*.45)}" width="{f(w*.12)}" height="{f(h*.45)}" fill="{trunk}"/>'
            f'<ellipse cx="{f(cx)}" cy="{f(base-h*.62)}" rx="{f(w/2)}" ry="{f(h*.38)}" fill="{fill}"/>')

def conifer(cx, base, h, w, fill=BGT):
    return f'<path fill="{fill}" d="M{f(cx)} {f(base-h)} Q{f(cx+w*.62)} {f(base-h*.2)} {f(cx+w/2)} {f(base)} L{f(cx-w/2)} {f(base)} Q{f(cx-w*.62)} {f(base-h*.2)} {f(cx)} {f(base-h)} Z"/>'

def cloud(x, y, k=1):
    return (f'<g fill="#ffffff" opacity=".9"><ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(46*k)}" ry="{f(16*k)}"/>'
            f'<circle cx="{f(x-14*k)}" cy="{f(y-10*k)}" r="{f(18*k)}"/><circle cx="{f(x+14*k)}" cy="{f(y-14*k)}" r="{f(22*k)}"/></g>')

def backdrop(W, H, gy, hills=True, sun=(0.82, 0.18)):
    s = [f'<rect width="{W}" height="{H}" fill="{SKY}"/>',
         f'<circle cx="{f(W*sun[0])}" cy="{f(H*sun[1])}" r="{f(H*.07)}" fill="#f4e7b0"/>',
         cloud(W*.18, H*.16, H/600), cloud(W*.62, H*.10, H/800)]
    if hills:
        s.append(f'<path fill="{HILL}" d="M0 {f(gy-H*.10)} Q{f(W*.25)} {f(gy-H*.22)} {f(W*.5)} {f(gy-H*.09)} T{W} {f(gy-H*.12)} L{W} {gy} L0 {gy} Z"/>')
    s.append(f'<rect y="{gy}" width="{W}" height="{H-gy}" fill="{GRASS}"/>')
    s.append(f'<rect y="{gy}" width="{W}" height="6" fill="{GRASS2}"/>')
    return "".join(s)

def limb(x1, y1, x2, y2, w, c):
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{c}" stroke-width="{f(w)}" stroke-linecap="round"/>'

def worker(x, y, k=1, arms=((-30, 30), (30, 30)), legs=True, flip=False):
    """Silhouette d'ouvrier sans visage, pieds en (x, y). arms : (angle épaule->coude, angle coude->main) en degrés, 0 = vers le bas."""
    g = []
    hip = y - 46*k; sh = y - 92*k
    if legs:
        g += [limb(x-7*k, hip, x-9*k, y-4*k, 13*k, DK), limb(x+7*k, hip, x+9*k, y-4*k, 13*k, DK),
              f'<rect x="{f(x-19*k)}" y="{f(y-7*k)}" width="{f(16*k)}" height="{f(7*k)}" rx="{f(2*k)}" fill="#2b2b2b"/>',
              f'<rect x="{f(x+3*k)}" y="{f(y-7*k)}" width="{f(16*k)}" height="{f(7*k)}" rx="{f(2*k)}" fill="#2b2b2b"/>']
    g.append(f'<rect x="{f(x-16*k)}" y="{f(sh-4*k)}" width="{f(32*k)}" height="{f(hip-sh+10*k)}" rx="{f(9*k)}" fill="{MAIN}"/>')
    g.append(f'<rect x="{f(x-16*k)}" y="{f(sh+16*k)}" width="{f(32*k)}" height="{f(6*k)}" fill="{ACC}"/>')  # bande haute visibilité
    hands = []
    for side, (a1, a2) in zip((-1, 1), arms):
        sx = x + side*12*k; sy = sh + 4*k
        r1, r2 = math.radians(a1), math.radians(a2)
        ex, ey = sx + math.sin(r1)*24*k, sy + math.cos(r1)*24*k
        hx, hy = ex + math.sin(r2)*22*k, ey + math.cos(r2)*22*k
        g += [limb(sx, sy, ex, ey, 10*k, MAIN), limb(ex, ey, hx, hy, 9*k, MAIN),
              f'<circle cx="{f(hx)}" cy="{f(hy)}" r="{f(5.5*k)}" fill="{SKIN}"/>']
        hands.append((hx, hy))
    hy0 = sh - 18*k
    g += [f'<circle cx="{f(x)}" cy="{f(hy0)}" r="{f(13*k)}" fill="{SKIN}"/>',
          f'<path fill="#f2f2f2" d="M{f(x-15*k)} {f(hy0-2*k)} A{f(15*k)} {f(15*k)} 0 0 1 {f(x+15*k)} {f(hy0-2*k)} Z"/>',
          f'<rect x="{f(x-18*k)}" y="{f(hy0-4*k)}" width="{f(36*k)}" height="{f(4*k)}" rx="{f(2*k)}" fill="#f2f2f2"/>',
          f'<rect x="{f(x-15*k)}" y="{f(hy0+1*k)}" width="{f(30*k)}" height="{f(5*k)}" rx="{f(2*k)}" fill="#e7a43a" opacity=".0"/>']
    body = "".join(g)
    if flip:
        body = f'<g transform="translate({f(2*x)} 0) scale(-1 1)">{body}</g>'
        hands = [(2*x - hx, hy) for hx, hy in hands]
    return body, hands

def house(x, base, w, h, roof=MAIN):
    return (f'<rect x="{f(x)}" y="{f(base-h)}" width="{f(w)}" height="{f(h)}" fill="#f7f4ec"/>'
            f'<path fill="{roof}" d="M{f(x-w*.08)} {f(base-h)} L{f(x+w/2)} {f(base-h-h*.62)} L{f(x+w*1.08)} {f(base-h)} Z"/>'
            f'<rect x="{f(x+w*.14)}" y="{f(base-h*.62)}" width="{f(w*.22)}" height="{f(h*.26)}" fill="{GREY}"/>'
            f'<rect x="{f(x+w*.6)}" y="{f(base-h*.55)}" width="{f(w*.22)}" height="{f(h*.55)}" fill="{WOOD}"/>')

def svg(W, H, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">'
            f'<title>{title}</title>{body}</svg>\n')

W, H, GY = 800, 600, 470

# ---------------------------------------------------------------- scènes
def elagage():
    s = [backdrop(W, H, GY)]
    s.append(round_tree(90, GY, 150, 110))
    s.append(oak(520, 210, 1.15, trunk_len=228))
    # camion nacelle
    s += [f'<rect x="60" y="{GY-62}" width="190" height="44" rx="6" fill="{MAIN}"/>',
          f'<path fill="{DK}" d="M250 {GY-62} h34 l22 26 v18 h-56 Z"/>',
          f'<rect x="262" y="{GY-56}" width="22" height="16" rx="2" fill="{GREY}"/>',
          f'<circle cx="100" cy="{GY-14}" r="18" fill="#2b2b2b"/><circle cx="100" cy="{GY-14}" r="7" fill="{GREY}"/>',
          f'<circle cx="270" cy="{GY-14}" r="18" fill="#2b2b2b"/><circle cx="270" cy="{GY-14}" r="7" fill="{GREY}"/>',
          f'<rect x="120" y="{GY-82}" width="40" height="22" rx="4" fill="{DK}"/>',
          limb(140, GY-76, 260, GY-230, 14, ACC), limb(260, GY-230, 352, GY-292, 11, ACC),
          f'<circle cx="140" cy="{GY-76}" r="10" fill="{DK}"/><circle cx="260" cy="{GY-230}" r="9" fill="{DK}"/>']
    # panier + élagueur avec perche
    bx, by = 340, GY-300
    wk, hands = worker(bx+30, by+40, 0.9, arms=((150, 160), (165, 175)), legs=False)
    s.append(wk)
    s.append(f'<rect x="{bx}" y="{by}" width="62" height="40" rx="4" fill="{WHITE}" stroke="{DK}" stroke-width="4"/>')
    hx, hy = hands[1]
    s.append(limb(hx-6, hy+20, hx+60, hy-56, 5, DK))
    s.append(f'<path fill="{GREY}" d="M{f(hx+56)} {f(hy-62)} l14 -6 l-4 14 Z"/>')
    # branche coupée qui tombe + balisage
    s.append(f'<g transform="rotate(-25 470 330)"><rect x="440" y="326" width="70" height="9" rx="4" fill="{WOOD2}"/>'
             f'<circle cx="512" cy="326" r="14" fill="{ACC}"/><circle cx="498" cy="318" r="10" fill="{ACC}"/></g>')
    for x in (610, 700):
        s.append(f'<path fill="#e8eef0" d="M{x-12} {GY+30} l12 -38 l12 38 Z"/><rect x="{x-8}" y="{GY+2}" width="16" height="6" fill="{ACC}"/>')
    s.append(limb(610, GY+10, 700, GY+10, 3, ACC))
    return "".join(s)

def abattage():
    s = [backdrop(W, H, GY)]
    s.append(house(40, GY, 170, 120))
    s.append(round_tree(740, GY, 130, 90))
    # tronc étêté avec quelques moignons
    tx = 470
    s += [f'<path fill="{WOOD2}" d="M{tx-24} {GY} L{tx-17} 140 L{tx+17} 140 L{tx+24} {GY} Z"/>',
          f'<ellipse cx="{tx}" cy="140" rx="17" ry="6" fill="{WOOD}"/>',
          limb(tx-14, 250, tx-56, 222, 12, WOOD2), f'<ellipse cx="{tx-57}" cy="221" rx="5" ry="7" fill="{WOOD}" transform="rotate(-55 {tx-57} 221)"/>',
          limb(tx+14, 300, tx+58, 276, 12, WOOD2), f'<ellipse cx="{tx+59}" cy="275" rx="5" ry="7" fill="{WOOD}" transform="rotate(-62 {tx+59} 275)"/>']
    # poulie + corde de rétention + tronçon descendu
    s += [f'<circle cx="{tx+10}" cy="168" r="7" fill="{DK}"/>',
          f'<path d="M{tx+16} 168 L{tx+120} 318" stroke="{ACC}" stroke-width="3.5" fill="none"/>',
          f'<g transform="rotate(-12 {tx+120} 340)"><rect x="{tx+90}" y="318" width="60" height="44" rx="6" fill="{WOOD2}"/>'
          f'<ellipse cx="{tx+150}" cy="340" rx="8" ry="22" fill="{WOOD}"/></g>']
    # grimpeur sur le tronc
    wk, hands = worker(tx-36, 226, 0.85, arms=((60, 80), (110, 140)), legs=True)
    s.append(f'<g transform="rotate(10 {tx-36} 226)">{wk}</g>')
    s.append(limb(tx-30, 160, tx+20, 175, 3, DK))  # longe
    # ouvrier au sol qui retient la corde
    wk2, h2 = worker(tx-120, GY, 0.95, arms=((120, 110), (110, 100)))
    s.append(wk2)
    s.append(f'<path d="M{tx+4} 168 L{f(h2[1][0])} {f(h2[1][1])}" stroke="{ACC}" stroke-width="3.5" fill="none"/>')
    # bûches
    for i, (x, y) in enumerate([(600, GY+40), (640, GY+40), (620, GY+16)]):
        s.append(f'<rect x="{x-20}" y="{y-24}" width="54" height="24" rx="5" fill="{WOOD2}"/><ellipse cx="{x+34}" cy="{y-12}" rx="7" ry="12" fill="{WOOD}"/>')
    return "".join(s)

def haie():
    s = [backdrop(W, H, GY)]
    s.append(round_tree(640, GY-150, 150, 120)); s.append(conifer(740, GY-150, 170, 60))
    # partie taillée (gauche) et partie à tailler (droite)
    s.append(f'<rect x="20" y="{GY-190}" width="430" height="190" rx="14" fill="{HEDGE}"/>')
    for i in range(9):
        s.append(f'<rect x="{30+i*47}" y="{GY-182}" width="6" height="170" rx="3" fill="{HEDGE2}" opacity=".6"/>')
    sh = "".join(f'<circle cx="{450+i*34}" cy="{GY-200-(18 if i%2 else 0)}" r="{40 if i%2 else 34}"/>' for i in range(10))
    s.append(f'<g fill="{HEDGE}">{sh}<rect x="440" y="{GY-210}" width="360" height="210"/></g>')
    s.append("".join(f'<ellipse cx="{470+i*40}" cy="{GY-226+(i%3)*10}" rx="9" ry="4" fill="{LEAF}" transform="rotate({(-1)**i*30} {470+i*40} {GY-226+(i%3)*10})"/>' for i in range(8)))
    # échafaudage léger
    s += [f'<rect x="372" y="{GY-120}" width="120" height="10" rx="3" fill="{GREY}"/>',
          limb(380, GY-110, 380, GY, 6, GREY), limb(484, GY-110, 484, GY, 6, GREY), limb(380, GY-60, 484, GY-110, 4, GREY)]
    wk, hands = worker(430, GY-120, 0.95, arms=((160, 175), (150, 150)), legs=True)
    s.append(wk)
    hx, hy = hands[1]
    s += [limb(hx-14, hy+4, hx+20, hy-14, 9, DK), limb(hx+16, hy-12, hx+90, hy-50, 6, GREY)]
    for i in range(7):
        s.append(f'<ellipse cx="{f(hx+40+i*9)}" cy="{f(hy-10+i*16)}" rx="6" ry="3" fill="{ACC}" transform="rotate({i*40} {f(hx+40+i*9)} {f(hy-10+i*16)})"/>')
    # brindilles au sol
    s.append("".join(f'<rect x="{60+i*55}" y="{GY+20+(i%3)*14}" width="22" height="4" rx="2" fill="{GRASS2}" transform="rotate({(-1)**i*20} {60+i*55} {GY+20})"/>' for i in range(12)))
    return "".join(s)

def dessouchage():
    s = [backdrop(W, H, GY)]
    s.append(round_tree(60, GY, 160, 100)); s.append(round_tree(740, GY, 150, 100))
    # souche + racines
    sx = 520
    s += [f'<path fill="{WOOD2}" d="M{sx-60} {GY+20} q10 -24 18 -70 h84 q8 46 18 70 Z"/>',
          f'<ellipse cx="{sx}" cy="{GY-50}" rx="42" ry="10" fill="{WOOD}"/>',
          f'<ellipse cx="{sx}" cy="{GY-50}" rx="26" ry="6" fill="none" stroke="{WOOD2}" stroke-width="2"/>',
          f'<path fill="{WOOD2}" d="M{sx-58} {GY+18} q-30 6 -50 26 h20 q14 -12 40 -14 Z M{sx+58} {GY+18} q34 4 58 24 h-22 q-16 -10 -40 -12 Z"/>']
    # rogneuse
    gx = 340
    s += [f'<rect x="{gx-90}" y="{GY-80}" width="150" height="56" rx="10" fill="{ACC}"/>',
          f'<rect x="{gx-70}" y="{GY-104}" width="70" height="28" rx="6" fill="{MAIN}"/>',
          f'<circle cx="{gx-60}" cy="{GY-16}" r="20" fill="#2b2b2b"/><circle cx="{gx-60}" cy="{GY-16}" r="8" fill="{GREY}"/>',
          f'<circle cx="{gx+30}" cy="{GY-16}" r="20" fill="#2b2b2b"/><circle cx="{gx+30}" cy="{GY-16}" r="8" fill="{GREY}"/>',
          limb(gx+40, GY-60, sx-44, GY-44, 16, MAIN),
          f'<circle cx="{sx-40}" cy="{GY-40}" r="22" fill="{GREY}"/><circle cx="{sx-40}" cy="{GY-40}" r="9" fill="{DK}"/>',
          limb(gx-90, GY-70, gx-140, GY-118, 6, DK)]
    for i in range(16):
        a = math.radians(-150 + i*9); r = 40 + (i*13) % 50
        x, y = sx-40 + math.cos(a)*r*1.4 + 40, GY-60 + math.sin(a)*r*.9
        s.append(f'<rect x="{f(x)}" y="{f(y)}" width="7" height="4" rx="1.5" fill="{WOOD}" transform="rotate({i*37} {f(x)} {f(y)})"/>')
    wk, hands = worker(gx-170, GY, 0.95, arms=((150, 120), (140, 110)))
    s.append(wk)
    s.append(f'<ellipse cx="{sx+20}" cy="{GY+40}" rx="90" ry="12" fill="{SOIL}" opacity=".8"/>')
    return "".join(s)

def tonte():
    s = [backdrop(W, H, 300)]
    s.append(house(560, 300, 160, 110, MAIN))
    s.append(round_tree(120, 300, 170, 120)); s.append(conifer(230, 300, 150, 60))
    s.append(f'<rect y="300" width="800" height="300" fill="{GRASS}"/>')
    for i in range(8):  # bandes de tonte en perspective
        x0 = -200 + i*150
        c = GRASS2 if i % 2 else "#9cc85e"
        s.append(f'<path fill="{c}" d="M{x0} 600 L{x0+150} 600 L{400+(x0+150-400)*.35} 300 L{400+(x0-400)*.35} 300 Z" opacity=".9"/>')
    s.append(f'<rect y="296" width="800" height="8" fill="{MAIN}" opacity=".25"/>')
    # tondeuse + jardinier
    mx, my = 470, 500
    wk, hands = worker(mx-150, my+18, 1.05, arms=((50, 70), (55, 75)))
    s.append(wk)
    hx, hy = hands[1]
    s += [f'<rect x="{mx-94}" y="{my-44}" width="46" height="42" rx="10" fill="{DK}"/>',
          f'<rect x="{mx-60}" y="{my-36}" width="120" height="40" rx="12" fill="{ACC}"/>',
          f'<rect x="{mx-30}" y="{my-54}" width="56" height="22" rx="8" fill="{MAIN}"/>',
          f'<circle cx="{mx-40}" cy="{my+6}" r="14" fill="#2b2b2b"/><circle cx="{mx+40}" cy="{my+6}" r="14" fill="#2b2b2b"/>',
          limb(mx-56, my-30, hx, hy, 6, "#2b2b2b"), limb(hx-4, hy-6, hx+4, hy+10, 6, "#2b2b2b")]
    for i in range(6):
        s.append(f'<rect x="{mx+66+i*10}" y="{my-10+i*5}" width="8" height="3" rx="1" fill="{GRASS2}" transform="rotate({i*30} {mx+66+i*10} {my-10+i*5})"/>')
    return "".join(s)

def pelouse():
    s = [backdrop(W, H, 330)]
    s.append(house(80, 330, 160, 110, MAIN)); s.append(round_tree(700, 330, 170, 120))
    s.append(f'<rect y="330" width="800" height="270" fill="{SOIL}"/>')
    # sillons ratissés
    for i in range(9):
        s.append(f'<path d="M0 {350+i*28} Q400 {340+i*28} 800 {352+i*28}" stroke="{SOIL2}" stroke-width="3" fill="none"/>')
    # zone semée qui lève (droite)
    s.append(f'<path fill="{GRASS}" d="M470 330 L800 330 L800 600 L360 600 Z"/>')
    for i in range(60):
        x = 380 + (i*53) % 410; y = 360 + (i*37) % 230
        if x > 360 + (600-y)*-(110/270) + 470 - 360 + (y-330)*0 and x > 470 - (y-330)*110/270:
            s.append(f'<path d="M{x} {y} q-4 -12 -2 -18 M{x} {y} q4 -10 8 -14" stroke="#5e8f2c" stroke-width="2.5" fill="none" stroke-linecap="round"/>')
    # graines
    for i in range(40):
        x = 60 + (i*71) % 330; y = 350 + (i*43) % 230
        s.append(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#e9dcb4"/>')
    # jardinier qui sème, sac
    wk, hands = worker(260, 520, 1.05, arms=((20, 10), (110, 90)))
    s.append(wk)
    hx, hy = hands[1]
    for i in range(7):
        s.append(f'<circle cx="{f(hx+18+i*12)}" cy="{f(hy+10+i*i*2.2)}" r="2.6" fill="#e9dcb4"/>')
    s += [f'<path fill="{WHITE}" d="M120 540 l8 -60 h60 l8 60 Z"/>', f'<rect x="138" y="500" width="40" height="22" fill="{ACC}"/>',
          limb(60, 585, 220, 578, 5, WOOD2), f'<rect x="216" y="560" width="8" height="40" rx="3" fill="{DK}"/>']
    return "".join(s)

def terrassement():
    s = [backdrop(W, H, 380)]
    s.append(round_tree(90, 380, 170, 120)); s.append(conifer(700, 380, 170, 70))
    s.append(f'<rect y="380" width="800" height="220" fill="{GRASS}"/>')
    # terre : bosses à gauche, plat à droite
    s.append(f'<path fill="{SOIL}" d="M0 600 L0 450 Q80 400 160 440 Q230 470 300 430 Q360 400 420 470 L800 470 L800 600 Z"/>')
    s.append(f'<rect x="420" y="470" width="380" height="130" fill="{SOIL2}"/>')
    s.append(f'<rect x="420" y="466" width="380" height="8" fill="{SOIL}"/>')
    # cordeau de niveau
    s += [limb(440, 446, 780, 446, 2.5, WHITE), limb(440, 440, 440, 476, 5, WOOD2), limb(780, 440, 780, 476, 5, WOOD2)]
    # mini-pelle
    ex, ey = 520, 470
    s += [f'<rect x="{ex-70}" y="{ey-30}" width="150" height="28" rx="14" fill="#2b2b2b"/>',
          "".join(f'<circle cx="{ex-52+i*38}" cy="{ey-16}" r="9" fill="{GREY}"/>' for i in range(4)),
          f'<rect x="{ex-60}" y="{ey-74}" width="120" height="44" rx="8" fill="{ACC}"/>',
          f'<path fill="{ACC}" d="M{ex-40} {ey-74} v-58 h56 l14 58 Z"/>',
          f'<path fill="{GREY}" d="M{ex-30} {ey-124} h38 l10 42 h-48 Z" opacity=".9"/>',
          limb(ex-50, ey-60, ex-140, ey-150, 16, MAIN), limb(ex-140, ey-150, ex-220, ey-60, 13, MAIN),
          f'<circle cx="{ex-140}" cy="{ey-150}" r="9" fill="{DK}"/>',
          f'<path fill="{DK}" d="M{ex-222} {ey-70} l-38 14 q-6 30 22 36 l30 -10 Z"/>']
    wk, hands = worker(ex-12, ey-80, 0.62, arms=((20, 80), (-20, -80)), legs=False)
    s.append(wk)
    return "".join(s)

def cloture():
    s = [backdrop(W, H, GY)]
    s.append(round_tree(500, GY-100, 160, 110)); s.append(conifer(770, GY-100, 190, 60))
    s.append(f'<rect y="{GY-100}" width="800" height="{H-GY+100}" fill="{GRASS}"/>')
    # panneaux rigides
    top = GY-130
    for p in range(3):
        x0 = 30 + p*170
        s.append(f'<rect x="{x0}" y="{top}" width="160" height="120" fill="none" stroke="{DK}" stroke-width="4"/>')
        for i in range(1, 8):
            s.append(limb(x0+i*20, top, x0+i*20, top+120, 3, DK))
        for j in (40, 80):
            s.append(f'<path d="M{x0} {top+j} h160" stroke="{DK}" stroke-width="3"/>')
    for p in range(4):
        s.append(f'<rect x="{22+p*170}" y="{top-14}" width="14" height="{134+14}" rx="2" fill="{MAIN}"/>')
    # claustra occultant à droite
    cx0 = 540
    s.append(f'<rect x="{cx0}" y="{top-30}" width="200" height="160" fill="{WOOD}"/>')
    for i in range(8):
        s.append(f'<rect x="{cx0}" y="{top-30+i*20}" width="200" height="4" fill="{WOOD2}"/>')
    s += [f'<rect x="{cx0-12}" y="{top-40}" width="14" height="180" rx="2" fill="{DK}"/>',
          f'<rect x="{cx0+198}" y="{top-40}" width="14" height="180" rx="2" fill="{DK}"/>']
    # ouvrier avec niveau
    wk, hands = worker(300, GY+60, 1.0, arms=((30, 100), (-30, -100)))
    s.append(wk)
    ly = (hands[0][1] + hands[1][1]) / 2 - 4
    s += [f'<rect x="240" y="{f(ly-6)}" width="120" height="12" rx="3" fill="{ACC}"/>',
          f'<rect x="291" y="{f(ly-4)}" width="18" height="8" rx="3" fill="{WHITE}"/>',
          f'<circle cx="{f(hands[0][0])}" cy="{f(hands[0][1])}" r="5.5" fill="{SKIN}"/><circle cx="{f(hands[1][0])}" cy="{f(hands[1][1])}" r="5.5" fill="{SKIN}"/>']
    # rouleau de grillage + poteau au sol
    s += [f'<rect x="80" y="{GY+50}" width="90" height="46" rx="23" fill="{GREY}"/>',
          f'<ellipse cx="170" cy="{GY+73}" rx="14" ry="23" fill="#b2bcb0"/>',
          f'<rect x="200" y="{GY+82}" width="140" height="12" rx="2" fill="{MAIN}" transform="rotate(-6 200 {GY+82})"/>']
    return "".join(s)

def hero():
    W2, H2, G = 1600, 900, 700
    s = [backdrop(W2, H2, G, sun=(0.74, 0.2))]
    for x, h, w in [(80, 260, 180), (300, 200, 140), (1450, 300, 220)]:
        s.append(round_tree(x, G, h, w))
    s.append(conifer(1300, G, 260, 90))
    s.append(house(1080, G, 220, 160, MAIN))
    s.append(oak(800, 330, 1.75, trunk_len=212))
    # nacelle
    s += [f'<rect x="420" y="{G-80}" width="250" height="56" rx="8" fill="{MAIN}"/>',
          f'<path fill="{DK}" d="M670 {G-80} h44 l28 34 v22 h-72 Z"/>',
          f'<rect x="686" y="{G-72}" width="28" height="20" rx="3" fill="{GREY}"/>',
          f'<circle cx="480" cy="{G-18}" r="24" fill="#2b2b2b"/><circle cx="700" cy="{G-18}" r="24" fill="#2b2b2b"/>',
          limb(520, G-100, 560, G-330, 18, DK), limb(560, G-330, 610, G-450, 14, DK),
          f'<circle cx="560" cy="{G-330}" r="12" fill="{DK}"/>']
    wk, hands = worker(640, G-430, 1.1, arms=((150, 160), (165, 175)), legs=False)
    s.append(wk)
    s.append(f'<rect x="602" y="{G-480}" width="80" height="50" rx="5" fill="{WHITE}" stroke="{DK}" stroke-width="5"/>')
    hx, hy = hands[1]
    s += [limb(hx-6, hy+24, hx+80, hy-70, 6, DK)]
    # haie basse en bas à gauche
    s.append(f'<rect x="0" y="{G-70}" width="380" height="70" rx="16" fill="{HEDGE}"/>')
    return W2, H2, "".join(s)

SCENES = {
    "illus-elagage": (elagage, "Illustration : élagage d'un arbre à la nacelle"),
    "illus-abattage": (abattage, "Illustration : abattage d'un arbre par démontage avec rétention"),
    "illus-taille-haie": (haie, "Illustration : taille d'une haie au taille-haie"),
    "illus-dessouchage": (dessouchage, "Illustration : rognage d'une souche à la rogneuse"),
    "illus-tonte": (tonte, "Illustration : tonte d'une pelouse"),
    "illus-creation-pelouse": (pelouse, "Illustration : semis d'une nouvelle pelouse"),
    "illus-terrassement": (terrassement, "Illustration : mise à niveau d'un terrain à la mini-pelle"),
    "illus-cloture": (cloture, "Illustration : pose d'une clôture rigide et d'un claustra"),
}

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "out"; os.makedirs(out, exist_ok=True)
    for name, (fn, title) in SCENES.items():
        open(f"{out}/{name}.svg", "w").write(svg(W, H, fn(), title))
    W2, H2, body = hero()
    open(f"{out}/hero-elagage.svg", "w").write(svg(W2, H2, body, "Illustration : élagueur en nacelle dans un grand arbre"))
    print("ok")
