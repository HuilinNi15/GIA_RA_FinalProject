import socket
import time

# Dirección IP del robot UR
HOST = "10.10.73.239"

# Puerto del servidor en el robot
PORT = 30002

# Scripts para abrir y cerrar la pinza
Abrir_pinza = 'pinza40UR3.py'
Cerrar_pinza = 'pinza10UR3.py'

# Función para enviar una trayectoria en espacio de configuraciones a la controladora del robot
def send_joint_path(path, sock):
    for joint_config in path:
        print(joint_config)
        sock.send(f"movej({joint_config}, a=0.5, v=0.5)".encode() + "\n".encode())
        time.sleep(1)

# Conexión via socket a la controladora del robot
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Trayectoria -- configuraciones (variables ctoria del robot real con la trayectoria del robot simulado en Kautham.# 
# Comenta si observas alguna diferencia y razónaloarticulares, en radianes)
path1 = [
    [2.2254700660705566, -0.9299110174179077, 0.6956869959831238, -1.3182499408721924, -1.515470027923584, -0.9171689748764038],
    [2.2639999389648438, -0.9431059956550598, 0.7356200218200684, -1.3816699981689453, -1.4958200454711914, -0.8750370144844055],
    [2.3025400638580322, -0.9563009738922119, 0.7755540013313293, -1.445099949836731, -1.4761600494384766, -0.8329039812088013],
    [2.3410799503326416, -0.9694949984550476, 0.8154870271682739, -1.5085200071334839, -1.4565099477767944, -0.790772020816803],
    [2.37962007522583, -0.9826899766921997, 0.8554210066795349, -1.5719499588012695, -1.4368599653244019, -0.7486389875411987],
    [2.418149948120117, -0.9958850145339966, 0.8953539729118347, -1.6353700160980225, -1.4172099828720093, -0.7065060138702393]
]

path2 = [
    [2.418149948120117, -0.9958850145339966, 0.8953539729118347, -1.6353700160980225, -1.4172099828720093, -0.7065060138702393],
    [2.418149948120117, -0.990822970867157, 0.9887869954109192, -1.733929991722107, -1.417330026626587, -0.7061589956283569],
    [2.418149948120117, -0.9857609868049622, 1.0822199583053589, -1.8324799537658691, -1.4174400568008423, -0.7058110237121582],
    [2.418149948120117, -0.9806979894638062, 1.1756500005722046, -1.931030035018921, -1.4175599813461304, -0.7054640054702759]
]

path3 = [
    [2.418149948120117, -0.9806979894638062, 1.1756500005722046, -1.931030035018921, -1.4175599813461304, -0.7054640054702759],
    [2.418149948120117, -0.983735978603363, 1.1195900440216064, -1.871899962425232, -1.417490005493164, -0.705672025680542],
    [2.418149948120117, -0.9867730140686035, 1.0635299682617188, -1.8127700090408325, -1.4174200296401978, -0.7058809995651245],
    [2.418149948120117, -0.9898099899291992, 1.0074700117111206, -1.753640055656433, -1.4173500537872314, -0.7060890197753906],
    [2.418149948120117, -0.9928479790687561, 0.9514139890670776, -1.6945099830627441, -1.4172799587249756, -0.7062979936599731],
    [2.418149948120117, -0.9958850145339966, 0.8953539729118347, -1.6353700160980225, -1.4172099828720093, -0.7065060138702393],
    [2.418149948120117, -0.9958850145339966, 0.8953539729118347, -1.6353700160980225, -1.4172099828720093, -0.7065060138702393],
    [2.4886701107025146, -0.991782009601593, 0.8577430248260498, -1.5675699710845947, -1.4388500452041626, -0.6329429745674133],
    [2.5591800212860107, -0.9876790046691895, 0.8201320171356201, -1.4997600317001343, -1.4604899883270264, -0.559378981590271],
    [2.5591800212860107, -0.9876790046691895, 0.8201320171356201, -1.4997600317001343, -1.4604899883270264, -0.559378981590271],
    [2.5591800212860107, -0.9876449704170227, 0.8864189982414246, -1.5660799741744995, -1.4605599641799927, -0.5591689944267273],
    [2.5591800212860107, -0.9876109957695007, 0.9527069926261902, -1.6324000358581543, -1.4606300592422485, -0.5589600205421448],
    [2.5591800212860107, -0.9875770211219788, 1.0189900398254395, -1.6987299919128418, -1.4607000350952148, -0.5587499737739563],
    [2.5591800212860107, -0.987542986869812, 1.085279941558838, -1.7650500535964966, -1.4607700109481812, -0.5585399866104126]
]

path4 = [
    [2.5591800212860107, -0.98750901222229, 1.1515699625015259, -1.8313699960708618, -1.4608399868011475, -0.5583299994468689],
    [2.5591800212860107, -0.9875659942626953, 1.0410900115966797, -1.720829963684082, -1.4607199430465698, -0.55867999792099],
    [2.5591800212860107, -0.9876220226287842, 0.9306110143661499, -1.6102999448776245, -1.460610032081604, -0.5590299963951111],
    [2.5591800212860107, -0.9876790046691895, 0.8201320171356201, -1.4997600317001343, -1.4604899883270264, -0.559378981590271]
]

path5 = [
    [2.5591800212860107, -0.9876790046691895, 0.8201320171356201, -1.4997600317001343, -1.4604899883270264, -0.559378981590271],
    [2.5600500106811523, -1.0419600009918213, 0.8990200161933899, -1.5229500532150269, -1.4621000289916992, -0.5593209862709045],
    [2.560920000076294, -1.0962400436401367, 0.9779090285301208, -1.5461499691009521, -1.4637099504470825, -0.5592619776725769],
    [2.561800003051758, -1.1505199670791626, 1.0568000078201294, -1.5693399906158447, -1.4653199911117554, -0.559203028678894],
    [2.5626699924468994, -1.204800009727478, 1.1356899738311768, -1.5925300121307373, -1.4669300317764282, -0.5591449737548828],
    [2.563539981842041, -1.2590800523757935, 1.2145800590515137, -1.6157300472259521, -1.4685399532318115, -0.5590860247612],
    [2.564419984817505, -1.3133599758148193, 1.2934600114822388, -1.6389199495315552, -1.4701499938964844, -0.5590270161628723],
    [2.5652899742126465, -1.3676400184631348, 1.3723499774932861, -1.66211998462677, -1.4717600345611572, -0.5589690208435059],
    [2.566159963607788, -1.4219199419021606, 1.4512399435043335, -1.6853100061416626, -1.4733699560165405, -0.5589100122451782],
    [2.5670299530029297, -1.476199984550476, 1.5301300287246704, -1.7085000276565552, -1.4749799966812134, -0.5588510036468506]
]

path6 = [
    [2.5670299530029297, -1.476199984550476, 1.5301300287246704, -1.7085000276565552, -1.4749799966812134, -0.5588510036468506],
    [2.5670299530029297, -1.4525500535964966, 1.6452399492263794, -1.8473399877548218, -1.4751499891281128, -0.5583299994468689],
    [2.5670299530029297, -1.4289000034332275, 1.7603399753570557, -1.9861799478530884, -1.4753299951553345, -0.5578089952468872]
 ]
 
path7 = [
    [2.5670299530029297, -1.4289000034332275, 1.7603399753570557, -1.9861799478530884, -1.4753299951553345, -0.5578089952468872],
    [2.5670299530029297, -1.4407299757003784, 1.7027900218963623, -1.916759967803955, -1.4752399921417236, -0.5580689907073975],
    [2.5670299530029297, -1.4525500535964966, 1.6452399492263794, -1.8473399877548218, -1.4751499891281128, -0.5583299994468689],
    [2.5670299530029297, -1.4643700122833252, 1.5876799821853638, -1.7779200077056885, -1.4750699996948242, -0.5585910081863403],
    [2.5670299530029297, -1.476199984550476, 1.5301300287246704, -1.7085000276565552, -1.4749799966812134, -0.5588510036468506],
    [2.5670299530029297, -1.476199984550476, 1.5301300287246704, -1.7085000276565552, -1.4749799966812134, -0.5588510036468506],
    [2.517519950866699, -1.454319953918457, 1.4560099840164185, -1.6135599613189697, -1.505579948425293, -0.5991119742393494],
    [2.4680099487304688, -1.4324500560760498, 1.381890058517456, -1.5186100006103516, -1.536180019378662, -0.6393730044364929],
    [2.4184999465942383, -1.410580039024353, 1.3077800273895264, -1.4236600399017334, -1.5667799711227417, -0.6796330213546753],
    [2.4184999465942383, -1.410580039024353, 1.3077800273895264, -1.4236600399017334, -1.5667799711227417, -0.6796330213546753],
    [2.418529987335205, -1.405750036239624, 1.3655699491500854, -1.4862899780273438, -1.5668100118637085, -0.6794000267982483],
    [2.418560028076172, -1.400920033454895, 1.4233700037002563, -1.5489200353622437, -1.5668400526046753, -0.6791660189628601],
    [2.4185900688171387, -1.396090030670166, 1.4811700582504272, -1.611549973487854, -1.5668699741363525, -0.6789330244064331],
    [2.4186201095581055, -1.391260027885437, 1.5389699935913086, -1.674180030822754, -1.5669000148773193, -0.6786990165710449],
    [2.418649911880493, -1.386430025100708, 1.5967700481414795, -1.7368099689483643, -1.5669300556182861, -0.6784660220146179]
]

path8 = [
    [2.4186699390411377, -1.381600022315979, 1.6545699834823608, -1.7994400262832642, -1.5669599771499634, -0.6782320141792297],
    [2.4186201095581055, -1.391260027885437, 1.5389699935913086, -1.674180030822754, -1.5669000148773193, -0.6786990165710449],
    [2.418560028076172, -1.400920033454895, 1.4233700037002563, -1.5489200353622437, -1.5668400526046753, -0.6791660189628601],
    [2.4184999465942383, -1.410580039024353, 1.3077800273895264, -1.4236600399017334, -1.5667799711227417, -0.6796330213546753]
]

path9 = [
    [2.4184999465942383, -1.410580039024353, 1.3077800273895264, -1.4236600399017334, -1.5667799711227417, -0.6796330213546753],
    [2.397059917449951, -1.3571699857711792, 1.2397700548171997, -1.4119499921798706, -1.561079978942871, -0.706026017665863],
    [2.375610113143921, -1.303760051727295, 1.1717599630355835, -1.4002399444580078, -1.5553799867630005, -0.7324190139770508],
    [2.3541600704193115, -1.250349998474121, 1.1037499904632568, -1.3885300159454346, -1.5496799945831299, -0.7588120102882385],
    [2.332710027694702, -1.1969499588012695, 1.0357400178909302, -1.3768099546432495, -1.543969988822937, -0.7852050065994263],
    [2.3112599849700928, -1.1435400247573853, 0.9677259922027588, -1.3651000261306763, -1.5382699966430664, -0.811598002910614],
    [2.2898099422454834, -1.090129971504211, 0.8997160196304321, -1.3533899784088135, -1.5325700044631958, -0.8379909992218018],
    [2.268359899520874, -1.0367300510406494, 0.8317070007324219, -1.3416800498962402, -1.5268700122833252, -0.8643839955329895],
    [2.246920108795166, -0.9833179712295532, 0.7636970281600952, -1.3299599885940552, -1.5211700201034546, -0.8907759785652161],
    [2.2254700660705566, -0.9299110174179077, 0.6956869959831238, -1.3182499408721924, -1.515470027923584, -0.9171689748764038]
]

path10 = [
    [2.2254700660705566, -0.9299110174179077, 0.6956869959831238, -1.3182499408721924, -1.515470027923584, -0.9171689748764038],
    [2.2254700660705566, -0.9382299780845642, 0.8104720115661621, -1.4247100353240967, -1.515470027923584, -0.9167630076408386],
    [2.2254700660705566, -0.9465489983558655, 0.9252579808235168, -1.5311800241470337, -1.515470027923584, -0.9163569808006287],
    [2.2254700660705566, -0.9548680186271667, 1.0400400161743164, -1.6376399993896484, -1.515470027923584, -0.9159500002861023]
]

path11 = [
    [2.2254700660705566, -0.9548680186271667, 1.0400400161743164, -1.6376399993896484, -1.515470027923584, -0.9159500002861023],
    [2.2254700660705566, -0.9498770236968994, 0.9711719751358032, -1.5737600326538086, -1.515470027923584, -0.9161940217018127],
    [2.2254700660705566, -0.9448860287666321, 0.902301013469696, -1.5098899602890015, -1.515470027923584, -0.9164379835128784],
    [2.2254700660705566, -0.9398940205574036, 0.8334289789199829, -1.4460099935531616, -1.515470027923584, -0.9166820049285889],
    [2.2254700660705566, -0.9349030256271362, 0.7645580172538757, -1.3821300268173218, -1.515470027923584, -0.9169260263442993],
    [2.2254700660705566, -0.9299110174179077, 0.6956869959831238, -1.3182499408721924, -1.515470027923584, -0.9171689748764038],
    [2.2254700660705566, -0.9299110174179077, 0.6956869959831238, -1.3182499408721924, -1.515470027923584, -0.9171689748764038],
    [2.2930099964141846, -0.9896020293235779, 0.7829539775848389, -1.3650699853897095, -1.5029000043869019, -0.8401560187339783],
    [2.3605599403381348, -1.0492899417877197, 0.8702210187911987, -1.4118900299072266, -1.4903299808502197, -0.763143002986908],
    [2.428100109100342, -1.1089799404144287, 0.9574880003929138, -1.4586999416351318, -1.4777699708938599, -0.6861299872398376],
    [2.4956400394439697, -1.1686700582504272, 1.04475998878479, -1.505519986152649, -1.4651999473571777, -0.6091169714927673],
    [2.4956400394439697, -1.1686700582504272, 1.04475998878479, -1.505519986152649, -1.4651999473571777, -0.6091169714927673],
    [2.5096399784088135, -1.1648999452590942, 1.111989974975586, -1.5765600204467773, -1.4652700424194336, -0.6088730096817017],
    [2.5236399173736572, -1.1611299514770508, 1.1792199611663818, -1.6475900411605835, -1.4653400182724, -0.6086300015449524],
    [2.53764009475708, -1.1573599576950073, 1.2464499473571777, -1.7186299562454224, -1.4654099941253662, -0.6083859801292419],
    [2.5516300201416016, -1.1535899639129639, 1.3136800527572632, -1.7896599769592285, -1.4654799699783325, -0.6081420183181763]
]

path12 = [
    [2.5656299591064453, -1.1498199701309204, 1.380910038948059, -1.860700011253357, -1.4655499458312988, -0.6078979969024658],
    [2.54229998588562, -1.1561100482940674, 1.2688599824905396, -1.742300033569336, -1.465440034866333, -0.6083049774169922],
    [2.518970012664795, -1.1623899936676025, 1.1568100452423096, -1.6239099502563477, -1.4653199911117554, -0.6087110042572021],
    [2.4956400394439697, -1.1686700582504272, 1.04475998878479, -1.505519986152649, -1.4651999473571777, -0.6091169714927673]
]

path13 = [
    [2.4956400394439697, -1.1686700582504272, 1.04475998878479, -1.505519986152649, -1.4651999473571777, -0.6091169714927673],
    [2.457050085067749, -1.134559988975525, 0.9948890209197998, -1.4787700176239014, -1.4723800420761108, -0.653124988079071],
    [2.418450117111206, -1.100450038909912, 0.9450219869613647, -1.4520100355148315, -1.4795600175857544, -0.6971319913864136],
    [2.379849910736084, -1.066349983215332, 0.8951550126075745, -1.4252599477767944, -1.486739993095398, -0.7411400079727173],
    [2.3412599563598633, -1.0322400331497192, 0.8452879786491394, -1.3985099792480469, -1.4939199686050415, -0.7851470112800598],
    [2.3026599884033203, -0.9981290102005005, 0.7954210042953491, -1.3717600107192993, -1.5011099576950073, -0.8291540145874023],
    [2.2640600204467773, -0.9640200138092041, 0.7455539703369141, -1.3450000286102295, -1.5082900524139404, -0.8731619715690613],
    [2.2254700660705566, -0.9299110174179077, 0.6956869959831238, -1.3182499408721924, -1.515470027923584, -0.9171689748764038]
]


# Se envia la trayectoria a la controladora del robot
send_joint_path(path1, sock) # Transit
send_joint_path(path2, sock) # Transit

# Enviar archivo script cerrar pinza
with open(Cerrar_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

# Se envia la trayectoria a la controladora del robot
send_joint_path(path3, sock) # Transfer

# Enviar archivo script abrir pinza
with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

# Se envia la trayectoria a la controladora del robot
send_joint_path(path4, sock) # Transit
send_joint_path(path5, sock) # Transit
send_joint_path(path6, sock) # Transit

# Enviar archivo script cerrar pinza
with open(Cerrar_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

# Se envia la trayectoria a la controladora del robot
send_joint_path(path7, sock) # Transfer

# Enviar archivo script abrir pinza
with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

# Se envia la trayectoria a la controladora del robot
send_joint_path(path8, sock) # Transit
send_joint_path(path9, sock) # Transit
send_joint_path(path10, sock) # Transit

# Enviar archivo script cerrar pinza
with open(Cerrar_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

# Se envia la trayectoria a la controladora del robot
send_joint_path(path11, sock) # Transfer

# Enviar archivo script abrir pinza
with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

# Se envia la trayectoria a la controladora del robot
send_joint_path(path12, sock) # Transit
send_joint_path(path13, sock) # Transit

# Mensaje que se imprime cuando se finaliza la ejecución
# de la trayectoria
print("Trayectoria finalizada")

data = sock.recv(1024)

# Se cierra la conexión
sock.close()
