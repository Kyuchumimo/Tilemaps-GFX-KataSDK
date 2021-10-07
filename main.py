###DEFINITIONS###
import katagames_sdk.engine as kataen
#import sys
import copy
pygame = kataen.import_pygame()
EventReceiver = kataen.EventReceiver
EngineEvTypes = kataen.EngineEvTypes
scr_size=None

#VARIABLE DECLARATION
p = {'x':0,'y':0}
sxymap = {'pos':[0, 0]}
varmap = {'x':0,'y':0,'w':20,'h':18,'sx':0,'sy':0,'colorkey':None,'scale':1,'remap':None}
t=0
xm=0
ym=0

pal0 = [(62,13,103),(241,29,124),(49,214,204),(251,233,138)]

#TITLE
m0 = [ [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,96,97,98,99],
   [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,112,113,114,115],
   [32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,128,129,130,131],
   [48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,144,145,146,147],
   [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,160,161,162,163],
   [80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,176,177,178,179],
   [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100],
   [101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101],
   [116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116],
   [117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117,117],
   [132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132],
   [133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133,133],
   [102,103,104,105,106,107,108,109,110,111,102,103,104,105,106,107,108,109,110,111],
   [118,119,120,121,122,123,124,125,126,127,118,119,120,121,122,123,124,125,126,127],
   [134,135,136,137,138,139,140,141,142,143,134,135,136,137,138,139,140,141,142,143],
   [150,151,152,153,154,155,156,157,158,159,150,151,152,153,154,155,156,157,158,159],
   [166,167,168,169,170,171,172,173,174,175,166,167,168,169,170,171,172,173,174,175],
   [182,183,184,185,186,187,188,189,190,191,182,183,184,185,186,187,188,189,190,191] ]

VRAM = copy.deepcopy(m0)

class View(EventReceiver):
  
  def __init__(self):
    super().__init__()
  def proc_event(self, ev, source):
    #ASSETS
    chr0 = pygame.image.load_basic('assets/0.bmp')
    chr1 = pygame.image.load_basic('assets/1.bmp')
    chr2 = pygame.image.load_basic('assets/2.bmp')
    chr3 = pygame.image.load_basic('assets/3.bmp')
    chr4 = pygame.image.load_basic('assets/4.bmp')
    chr5 = pygame.image.load_basic('assets/5.bmp')
    chr6 = pygame.image.load_basic('assets/6.bmp')
    chr7 = pygame.image.load_basic('assets/7.bmp')
    chr8 = pygame.image.load_basic('assets/8.bmp')
    chr9 = pygame.image.load_basic('assets/9.bmp')
    chr10 = pygame.image.load_basic('assets/10.bmp')
    chr11 = pygame.image.load_basic('assets/11.bmp')
    chr12 = pygame.image.load_basic('assets/12.bmp')
    chr13 = pygame.image.load_basic('assets/13.bmp')
    chr14 = pygame.image.load_basic('assets/14.bmp')
    chr15 = pygame.image.load_basic('assets/15.bmp')
    chr16 = pygame.image.load_basic('assets/16.bmp')
    chr17 = pygame.image.load_basic('assets/17.bmp')
    chr18 = pygame.image.load_basic('assets/18.bmp')
    chr19 = pygame.image.load_basic('assets/19.bmp')
    chr20 = pygame.image.load_basic('assets/20.bmp')
    chr21 = pygame.image.load_basic('assets/21.bmp')
    chr22 = pygame.image.load_basic('assets/22.bmp')
    chr23 = pygame.image.load_basic('assets/23.bmp')
    chr24 = pygame.image.load_basic('assets/24.bmp')
    chr25 = pygame.image.load_basic('assets/25.bmp')
    chr26 = pygame.image.load_basic('assets/26.bmp')
    chr27 = pygame.image.load_basic('assets/27.bmp')
    chr28 = pygame.image.load_basic('assets/28.bmp')
    chr29 = pygame.image.load_basic('assets/29.bmp')
    chr30 = pygame.image.load_basic('assets/30.bmp')
    chr31 = pygame.image.load_basic('assets/31.bmp')
    chr32 = pygame.image.load_basic('assets/32.bmp')
    chr33 = pygame.image.load_basic('assets/33.bmp')
    chr34 = pygame.image.load_basic('assets/34.bmp')
    chr35 = pygame.image.load_basic('assets/35.bmp')
    chr36 = pygame.image.load_basic('assets/36.bmp')
    chr37 = pygame.image.load_basic('assets/37.bmp')
    chr38 = pygame.image.load_basic('assets/38.bmp')
    chr39 = pygame.image.load_basic('assets/39.bmp')
    chr40 = pygame.image.load_basic('assets/40.bmp')
    chr41 = pygame.image.load_basic('assets/41.bmp')
    chr42 = pygame.image.load_basic('assets/42.bmp')
    chr43 = pygame.image.load_basic('assets/43.bmp')
    chr44 = pygame.image.load_basic('assets/44.bmp')
    chr45 = pygame.image.load_basic('assets/45.bmp')
    chr46 = pygame.image.load_basic('assets/46.bmp')
    chr47 = pygame.image.load_basic('assets/47.bmp')
    chr48 = pygame.image.load_basic('assets/48.bmp')
    chr49 = pygame.image.load_basic('assets/49.bmp')
    chr50 = pygame.image.load_basic('assets/50.bmp')
    chr51 = pygame.image.load_basic('assets/51.bmp')
    chr52 = pygame.image.load_basic('assets/52.bmp')
    chr53 = pygame.image.load_basic('assets/53.bmp')
    chr54 = pygame.image.load_basic('assets/54.bmp')
    chr55 = pygame.image.load_basic('assets/55.bmp')
    chr56 = pygame.image.load_basic('assets/56.bmp')
    chr57 = pygame.image.load_basic('assets/57.bmp')
    chr58 = pygame.image.load_basic('assets/58.bmp')
    chr59 = pygame.image.load_basic('assets/59.bmp')
    chr60 = pygame.image.load_basic('assets/60.bmp')
    chr61 = pygame.image.load_basic('assets/61.bmp')
    chr62 = pygame.image.load_basic('assets/62.bmp')
    chr63 = pygame.image.load_basic('assets/63.bmp')
    chr64 = pygame.image.load_basic('assets/64.bmp')
    chr65 = pygame.image.load_basic('assets/65.bmp')
    chr66 = pygame.image.load_basic('assets/66.bmp')
    chr67 = pygame.image.load_basic('assets/67.bmp')
    chr68 = pygame.image.load_basic('assets/68.bmp')
    chr69 = pygame.image.load_basic('assets/69.bmp')
    chr70 = pygame.image.load_basic('assets/70.bmp')
    chr71 = pygame.image.load_basic('assets/71.bmp')
    chr72 = pygame.image.load_basic('assets/72.bmp')
    chr73 = pygame.image.load_basic('assets/73.bmp')
    chr74 = pygame.image.load_basic('assets/74.bmp')
    chr75 = pygame.image.load_basic('assets/75.bmp')
    chr76 = pygame.image.load_basic('assets/76.bmp')
    chr77 = pygame.image.load_basic('assets/77.bmp')
    chr78 = pygame.image.load_basic('assets/78.bmp')
    chr79 = pygame.image.load_basic('assets/79.bmp')
    chr80 = pygame.image.load_basic('assets/80.bmp')
    chr81 = pygame.image.load_basic('assets/81.bmp')
    chr82 = pygame.image.load_basic('assets/82.bmp')
    chr83 = pygame.image.load_basic('assets/83.bmp')
    chr84 = pygame.image.load_basic('assets/84.bmp')
    chr85 = pygame.image.load_basic('assets/85.bmp')
    chr86 = pygame.image.load_basic('assets/86.bmp')
    chr87 = pygame.image.load_basic('assets/87.bmp')
    chr88 = pygame.image.load_basic('assets/88.bmp')
    chr89 = pygame.image.load_basic('assets/89.bmp')
    chr90 = pygame.image.load_basic('assets/90.bmp')
    chr91 = pygame.image.load_basic('assets/91.bmp')
    chr92 = pygame.image.load_basic('assets/92.bmp')
    chr93 = pygame.image.load_basic('assets/93.bmp')
    chr94 = pygame.image.load_basic('assets/94.bmp')
    chr95 = pygame.image.load_basic('assets/95.bmp')
    chr96 = pygame.image.load_basic('assets/96.bmp')
    chr97 = pygame.image.load_basic('assets/97.bmp')
    chr98 = pygame.image.load_basic('assets/98.bmp')
    chr99 = pygame.image.load_basic('assets/99.bmp')
    chr100 = pygame.image.load_basic('assets/100.bmp')
    chr101 = pygame.image.load_basic('assets/101.bmp')
    chr102 = pygame.image.load_basic('assets/102.bmp')
    chr103 = pygame.image.load_basic('assets/103.bmp')
    chr104 = pygame.image.load_basic('assets/104.bmp')
    chr105 = pygame.image.load_basic('assets/105.bmp')
    chr106 = pygame.image.load_basic('assets/106.bmp')
    chr107 = pygame.image.load_basic('assets/107.bmp')
    chr108 = pygame.image.load_basic('assets/108.bmp')
    chr109 = pygame.image.load_basic('assets/109.bmp')
    chr110 = pygame.image.load_basic('assets/110.bmp')
    chr111 = pygame.image.load_basic('assets/111.bmp')
    chr112 = pygame.image.load_basic('assets/112.bmp')
    chr113 = pygame.image.load_basic('assets/113.bmp')
    chr114 = pygame.image.load_basic('assets/114.bmp')
    chr115 = pygame.image.load_basic('assets/115.bmp')
    chr116 = pygame.image.load_basic('assets/116.bmp')
    chr117 = pygame.image.load_basic('assets/117.bmp')
    chr118 = pygame.image.load_basic('assets/118.bmp')
    chr119 = pygame.image.load_basic('assets/119.bmp')
    chr120 = pygame.image.load_basic('assets/120.bmp')
    chr121 = pygame.image.load_basic('assets/121.bmp')
    chr122 = pygame.image.load_basic('assets/122.bmp')
    chr123 = pygame.image.load_basic('assets/123.bmp')
    chr124 = pygame.image.load_basic('assets/124.bmp')
    chr125 = pygame.image.load_basic('assets/125.bmp')
    chr126 = pygame.image.load_basic('assets/126.bmp')
    chr127 = pygame.image.load_basic('assets/127.bmp')
    chr128 = pygame.image.load_basic('assets/128.bmp')
    chr129 = pygame.image.load_basic('assets/129.bmp')
    chr130 = pygame.image.load_basic('assets/130.bmp')
    chr131 = pygame.image.load_basic('assets/131.bmp')
    chr132 = pygame.image.load_basic('assets/132.bmp')
    chr133 = pygame.image.load_basic('assets/133.bmp')
    chr134 = pygame.image.load_basic('assets/134.bmp')
    chr135 = pygame.image.load_basic('assets/135.bmp')
    chr136 = pygame.image.load_basic('assets/136.bmp')
    chr137 = pygame.image.load_basic('assets/137.bmp')
    chr138 = pygame.image.load_basic('assets/138.bmp')
    chr139 = pygame.image.load_basic('assets/139.bmp')
    chr140 = pygame.image.load_basic('assets/140.bmp')
    chr141 = pygame.image.load_basic('assets/141.bmp')
    chr142 = pygame.image.load_basic('assets/142.bmp')
    chr143 = pygame.image.load_basic('assets/143.bmp')
    chr144 = pygame.image.load_basic('assets/144.bmp')
    chr145 = pygame.image.load_basic('assets/145.bmp')
    chr146 = pygame.image.load_basic('assets/146.bmp')
    chr147 = pygame.image.load_basic('assets/147.bmp')
    chr148 = pygame.image.load_basic('assets/148.bmp')
    chr149 = pygame.image.load_basic('assets/149.bmp')
    chr150 = pygame.image.load_basic('assets/150.bmp')
    chr151 = pygame.image.load_basic('assets/151.bmp')
    chr152 = pygame.image.load_basic('assets/152.bmp')
    chr153 = pygame.image.load_basic('assets/153.bmp')
    chr154 = pygame.image.load_basic('assets/154.bmp')
    chr155 = pygame.image.load_basic('assets/155.bmp')
    chr156 = pygame.image.load_basic('assets/156.bmp')
    chr157 = pygame.image.load_basic('assets/157.bmp')
    chr158 = pygame.image.load_basic('assets/158.bmp')
    chr159 = pygame.image.load_basic('assets/159.bmp')
    chr160 = pygame.image.load_basic('assets/160.bmp')
    chr161 = pygame.image.load_basic('assets/161.bmp')
    chr162 = pygame.image.load_basic('assets/162.bmp')
    chr163 = pygame.image.load_basic('assets/163.bmp')
    chr164 = pygame.image.load_basic('assets/164.bmp')
    chr165 = pygame.image.load_basic('assets/165.bmp')
    chr166 = pygame.image.load_basic('assets/166.bmp')
    chr167 = pygame.image.load_basic('assets/167.bmp')
    chr168 = pygame.image.load_basic('assets/168.bmp')
    chr169 = pygame.image.load_basic('assets/169.bmp')
    chr170 = pygame.image.load_basic('assets/170.bmp')
    chr171 = pygame.image.load_basic('assets/171.bmp')
    chr172 = pygame.image.load_basic('assets/172.bmp')
    chr173 = pygame.image.load_basic('assets/173.bmp')
    chr174 = pygame.image.load_basic('assets/174.bmp')
    chr175 = pygame.image.load_basic('assets/175.bmp')
    chr176 = pygame.image.load_basic('assets/176.bmp')
    chr177 = pygame.image.load_basic('assets/177.bmp')
    chr178 = pygame.image.load_basic('assets/178.bmp')
    chr179 = pygame.image.load_basic('assets/179.bmp')
    chr180 = pygame.image.load_basic('assets/180.bmp')
    chr181 = pygame.image.load_basic('assets/181.bmp')
    chr182 = pygame.image.load_basic('assets/182.bmp')
    chr183 = pygame.image.load_basic('assets/183.bmp')
    chr184 = pygame.image.load_basic('assets/184.bmp')
    chr185 = pygame.image.load_basic('assets/185.bmp')
    chr186 = pygame.image.load_basic('assets/186.bmp')
    chr187 = pygame.image.load_basic('assets/187.bmp')
    chr188 = pygame.image.load_basic('assets/188.bmp')
    chr189 = pygame.image.load_basic('assets/189.bmp')
    chr190 = pygame.image.load_basic('assets/190.bmp')
    chr191 = pygame.image.load_basic('assets/191.bmp')
    chr192 = pygame.image.load_basic('assets/192.bmp')
    chr193 = pygame.image.load_basic('assets/193.bmp')
    chr194 = pygame.image.load_basic('assets/194.bmp')
    chr195 = pygame.image.load_basic('assets/195.bmp')
    chr196 = pygame.image.load_basic('assets/196.bmp')
    chr197 = pygame.image.load_basic('assets/197.bmp')
    chr198 = pygame.image.load_basic('assets/198.bmp')
    chr199 = pygame.image.load_basic('assets/199.bmp')
    chr200 = pygame.image.load_basic('assets/200.bmp')
    chr201 = pygame.image.load_basic('assets/201.bmp')
    chr202 = pygame.image.load_basic('assets/202.bmp')
    chr203 = pygame.image.load_basic('assets/203.bmp')
    chr204 = pygame.image.load_basic('assets/204.bmp')
    chr205 = pygame.image.load_basic('assets/205.bmp')
    chr206 = pygame.image.load_basic('assets/206.bmp')
    chr207 = pygame.image.load_basic('assets/207.bmp')
    chr208 = pygame.image.load_basic('assets/208.bmp')
    chr209 = pygame.image.load_basic('assets/209.bmp')
    chr210 = pygame.image.load_basic('assets/210.bmp')
    chr211 = pygame.image.load_basic('assets/211.bmp')
    chr212 = pygame.image.load_basic('assets/212.bmp')
    chr213 = pygame.image.load_basic('assets/213.bmp')
    chr214 = pygame.image.load_basic('assets/214.bmp')
    chr215 = pygame.image.load_basic('assets/215.bmp')
    chr216 = pygame.image.load_basic('assets/216.bmp')
    chr217 = pygame.image.load_basic('assets/217.bmp')
    chr218 = pygame.image.load_basic('assets/218.bmp')
    chr219 = pygame.image.load_basic('assets/219.bmp')
    chr220 = pygame.image.load_basic('assets/220.bmp')
    chr221 = pygame.image.load_basic('assets/221.bmp')
    chr222 = pygame.image.load_basic('assets/222.bmp')
    chr223 = pygame.image.load_basic('assets/223.bmp')
    chr224 = pygame.image.load_basic('assets/224.bmp')
    chr225 = pygame.image.load_basic('assets/225.bmp')
    chr226 = pygame.image.load_basic('assets/226.bmp')
    chr227 = pygame.image.load_basic('assets/227.bmp')
    chr228 = pygame.image.load_basic('assets/228.bmp')
    chr229 = pygame.image.load_basic('assets/229.bmp')
    chr230 = pygame.image.load_basic('assets/230.bmp')
    chr231 = pygame.image.load_basic('assets/231.bmp')
    chr232 = pygame.image.load_basic('assets/232.bmp')
    chr233 = pygame.image.load_basic('assets/233.bmp')
    chr234 = pygame.image.load_basic('assets/234.bmp')
    chr235 = pygame.image.load_basic('assets/235.bmp')
    chr236 = pygame.image.load_basic('assets/236.bmp')
    chr237 = pygame.image.load_basic('assets/237.bmp')
    chr238 = pygame.image.load_basic('assets/238.bmp')
    chr239 = pygame.image.load_basic('assets/239.bmp')
    chr240 = pygame.image.load_basic('assets/240.bmp')
    chr241 = pygame.image.load_basic('assets/241.bmp')
    chr242 = pygame.image.load_basic('assets/242.bmp')
    chr243 = pygame.image.load_basic('assets/243.bmp')
    chr244 = pygame.image.load_basic('assets/244.bmp')
    chr245 = pygame.image.load_basic('assets/245.bmp')
    chr246 = pygame.image.load_basic('assets/246.bmp')
    chr247 = pygame.image.load_basic('assets/247.bmp')
    chr248 = pygame.image.load_basic('assets/248.bmp')
    chr249 = pygame.image.load_basic('assets/249.bmp')
    chr250 = pygame.image.load_basic('assets/250.bmp')
    chr251 = pygame.image.load_basic('assets/251.bmp')
    chr252 = pygame.image.load_basic('assets/252.bmp')
    chr253 = pygame.image.load_basic('assets/253.bmp')
    chr254 = pygame.image.load_basic('assets/254.bmp')
    chr255 = pygame.image.load_basic('assets/255.bmp')
    chr = [chr0,chr1,chr2,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr20,chr21,chr22,chr23,chr24,chr25,chr26,chr27,chr28,chr29,chr30,chr31,chr32,chr33,chr34,chr35,chr36,chr37,chr38,chr39,chr40,chr41,chr42,chr43,chr44,chr45,chr46,chr47,chr48,chr49,chr50,chr51,chr52,chr53,chr54,chr55,chr56,chr57,chr58,chr59,chr60,chr61,chr62,chr63,chr64,chr65,chr66,chr67,chr68,chr69,chr70,chr71,chr72,chr73,chr74,chr75,chr76,chr77,chr78,chr79,chr80,chr81,chr82,chr83,chr84,chr85,chr86,chr87,chr88,chr89,chr90,chr91,chr92,chr93,chr94,chr95,chr96,chr97,chr98,chr99,chr100,chr101,chr102,chr103,chr104,chr105,chr106,chr107,chr108,chr109,chr110,chr111,chr112,chr113,chr114,chr115,chr116,chr117,chr118,chr119,chr120,chr121,chr122,chr123,chr124,chr125,chr126,chr127,chr128,chr129,chr130,chr131,chr132,chr133,chr134,chr135,chr136,chr137,chr138,chr139,chr140,chr141,chr142,chr143,chr144,chr145,chr146,chr147,chr148,chr149,chr150,chr151,chr152,chr153,chr154,chr155,chr156,chr157,chr158,chr159,chr160,chr161,chr162,chr163,chr164,chr165,chr166,chr167,chr168,chr169,chr170,chr171,chr172,chr173,chr174,chr175,chr176,chr177,chr178,chr179,chr180,chr181,chr182,chr183,chr184,chr185,chr186,chr187,chr188,chr189,chr190,chr191,chr192,chr193,chr194,chr195,chr196,chr197,chr198,chr199,chr200,chr201,chr202,chr203,chr204,chr205,chr206,chr207,chr208,chr209,chr210,chr211,chr212,chr213,chr214,chr215,chr216,chr217,chr218,chr219,chr220,chr221,chr222,chr223,chr224,chr225,chr226,chr227,chr228,chr229,chr230,chr231,chr232,chr233,chr234,chr235,chr236,chr237,chr238,chr239,chr240,chr241,chr242,chr243,chr244,chr245,chr246,chr247,chr248,chr249,chr250,chr251,chr252,chr253,chr254,chr255]
    info_font = pygame.font.Font(None, 12)
    
#DRAW EVENT
    if ev.type == EngineEvTypes.PAINT:
#GRAPHICS        
      #TIC-80'S MAP() FUNCTION, https://github.com/nesbox/TIC-80/wiki/map
      """
      x : The leftmost map cell to be drawn.
      y : The uppermost map cell to be drawn.
      w : The number of cells to draw horizontally.
      h : The number of cells to draw vertically.
      sx : The screen x coordinate where drawing of the map section will start.
      sy : The screen y coordinate where drawing of the map section will start.
      colorkey : index (or array of indexes) of the color that will be used as transparent color. Not setting this parameter will make the map opaque.
      scale [UNUSED] : Map scaling.
      remap [PARTIAL] : An optional function called before every tile is drawn. Using this callback function you can show or hide tiles, create tile animations or flip/rotate tiles during the map rendering stage: callback [tile [x y] ] -> [tile [flip [rotate] ] ] 
      """
      def map(x,y,w=30,h=20,sx=0,sy=0,colorkey=None,scale=1,remap=None):
      
          PPU=copy.deepcopy(VRAM)
          if remap!=None: exec(remap)
          #if remap==None: remap=(VRAM,VRAM,VRAM)
    
          if colorkey!=None: ts.set_colorkey(colorkey)
    
          #TILE BASED BACKGROUND
          for i in range(y,y+h): #ROWS
              for j in range(x,x+w): #COLUMNS
   
                 ev.screen.blit(chr[PPU[i][j]],[(sx+(j*8))-(x*8),(sy+(i*8))-(y*8)]) #DRAW A MAP THROUGH A LIST OF INDEPENDENT IMAGES (MEDIUM)
      
      ev.screen.fill((255,255,255)) #FILL fill(color, rect=None, special_flags=0)
      #pygame.draw.circle(ev.screen, (0,0,0), p['pos'], 15) #CIRCLE circle(surface, color, center, radius)
      #ev.screen.blit(image.subsurface([0,0],[4,4]),[0,0]) #SUBSURFACE subsurface(Rect)
      
      map(0,0,20,18,sxymap['pos'][0],sxymap['pos'][1],None,1,
"""
if (VRAM[int((((ym%8)+(p['y']+15))//8)+(ym//8))][int((((xm%8)+(p['x']+8))//8)+(xm//8))]==18 or VRAM[int((((ym%8)+(p['y']+15))//8)+(ym//8))][int((((xm%8)+(p['x']+8))//8)+(xm//8))]==19 or VRAM[int((((ym%8)+(p['y']+15))//8)+(ym//8))][int((((xm%8)+(p['x']+8))//8)+(xm//8))]==34 or VRAM[int((((ym%8)+(p['y']+15))//8)+(ym//8))][int((((xm%8)+(p['x']+8))//8)+(xm//8))]==35):
 
 PPU[int((((ym%16)+(p['y']+15))//16*2)+(ym//16*2))][int((((xm%16)+(p['x']+8))//16*2)+(xm//16*2))]=48;
 PPU[int((((ym%16)+(p['y']+15))//16*2)+(ym//16*2))][int((((xm%16)+(p['x']+8))//16*2)+(xm//16*2))+1]=49;
 PPU[int((((ym%16)+(p['y']+15))//16*2)+(ym//16*2))+1][int((((xm%16)+(p['x']+8))//16*2)+(xm//16*2))]=64;
 PPU[int((((ym%16)+(p['y']+15))//16*2)+(ym//16*2))+1][int((((xm%16)+(p['x']+8))//16*2)+(xm//16*2))+1]=65
"""
)
      ev.screen.blit(info_font.render(str((p['x'],p['y'])),False,[252,252,252]),[0,0])
      ev.screen.blit(chr[0],[p['x'],p['y']])

class Ctrl(EventReceiver):
  def __init__(self):
    super().__init__()
  def proc_event(self, ev, source):
    global scr_size
    global t
#LOGIC EVENT
    if ev.type == EngineEvTypes.LOGICUPDATE:
#CONTROLS
      #if pygame.key.get_pressed()[pygame.K_ESCAPE]: sys.exit()
      
      if pygame.key.get_pressed()[pygame.K_UP]:
        p['y'] -= 1
      if pygame.key.get_pressed()[pygame.K_DOWN]:
        p['y'] += 1
      if pygame.key.get_pressed()[pygame.K_LEFT]:
        p['x'] -= 1
      if pygame.key.get_pressed()[pygame.K_RIGHT]:
        p['x'] += 1
      
      p['x'] = p['x'] % 152
      p['y'] = p['y'] % 128
      
      t+=1


###MAIN PROGRAM###
def run_game():
  global scr_size
  kataen.init(kataen.SUPER_RETRO_MODE)
  scr_size = kataen.get_screen().get_size()
  #INITIATION
  li_recv = [kataen.get_game_ctrl(), View(), Ctrl()]
  for recv_obj in li_recv:
    recv_obj.turn_on()
  #LOOP
  li_recv[0].loop()
  kataen.cleanup()

if __name__=='__main__':
  run_game()
