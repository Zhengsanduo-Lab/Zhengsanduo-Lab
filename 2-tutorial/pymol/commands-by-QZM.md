**Creator : QS&NYY**

**Date : 2024.02.10**

**E-mail : qiuzeming@nibs.ac.cn**

**Hope You Good Life**

pymol mouse control :

```
3-button viewing
L, R, M, wheeling : 左键，右键，中键，滚轮
L : rotating
R : Move Z
M : Move XY 
Wheeling : Slab
Shift + R : Clip #调整截面
Shift + L : + Box #选择 select
Shift + M : - Box #不选择 unselect
SingleClick + M : center #中心点

#              ^ Y
#              |
#              |
#              |
#              |----------> X
#             /
#            /
#           /
#          Z
```

Action ---> rename selection

Action ---> extract object

Action ---> copy to object

Action ---> zoom #居中放大

Action--->compute--->surface area

Wizard ---> Measure ---> distance, angle, dihedral, distance to ring

Setting ---> Edit all

File ---> export molecule --->all,enable(visible)

Wizard ---> Demo--->representation可以看好玩的东西

鼠标右击待移动的object,按住鼠标不放，移动鼠标，调整object在列表中顺序

如果分子名字太长，默认pymol右侧窗口太小，这样名字会看不清。 鼠标左键点击右小角，如图所示，按住不放，移动鼠标就可以调节窗口宽度了。

pymol command line:

```
cd D:/tmp
# 打开XXXX，命名为test
load ~/XXXX.pdb , test 

fetch XXXX

#合并A，B，C，成为complex
create complex , A B C 

# align A to B , B don't change position.
super A , B 

# super, cealign, align, pairfit, fit 是 align 命令

#调整display area width and height
viewpoint 900,1200 

#pml file : pymol macro language 打开log.pml中已经设定好的画图格式，！！！非常有用！！！
log-open log.pml 

#显示cartoon格式，as用新的representation代替旧的representation
as/show/hide cartoon/lines/sticks , object/all 

#选择residue 300和301，命名为tmp
select tmp , resi 300+301 

#居中放大tmp
zoom tmp 

#删除
delete selection-1 selection-2 selection-3
delete object-1 object-2 object-3

#改变颜色 1-100 残基，secondary structure helix、loop、beta sheet
color red/yellow/green/white/blue , all/object-1/resi 300+301/resi 1-100/ss h/ss l/ss s 

#激活和禁用object
enable/disable object-1

#禁用所有
disable 
disable all

#改变主链的N，CA，C，O颜色
color yellow, name n+ca+c+o  

#选择主链
select tmp, name n+ca+c+o 

#隐藏所有氢原子
hide hydro/h. 

#显示pdb中被定义为hetatm（ligand，H2O，Mg）的所有原子
show spheres, hetatm 

#选择所有hetatm原子，氢原子
select tmp , hetatm/hydro 

#选择helix、loop、beta sheet，unstruct part
select tmp , ss h/l/s/"" 

#选择全部的N，O，C，H，Mg原子
select tmp , symbol N/O/C/H/Mg 

#选择主链中的n，ca，c，o原子
select tmp , name n+ca+c+o 

#选择所有proline和lysine的原子
select tmp , resn pro+lys 

#选择前100个氨基酸
select tmp , resi 1-100 

#选择chain A
select tmp , chain A 

#选择sidechain，backbone
select tmp , sidechain/backbone 

#不选择1
select tmp , not 1 

#选择1 2 交集
select tmp , 1 and 2 

#选择1和2和3 并集
select tmp , 1 2 3 

#选择1和2和3 并集
select tmp , 1 or 2 or 3 

#选择1和2和3 并集
select tmp , 1+2+3 

#选择不严格的 交集
select tmp , sidechain in chain A 

#选择chain B中前100残基
select tmp , resi 1-100 and chain B 

#选择所有非蛋白小分子作为ligand
select ligand , hetatm 

#选择ligand附近5A内的原子 ，不包括ligand
select ligand-5 , ligand around 15 

# 选择AC附近5A内的原子，不包括ligand，且一定在Gs上的，命名为Gs-interaction-residue
select Gs-interaction-residue , Gs within 5 of AC

# 选择chain_A与chain_B的距离5A内的互作残基，命名为interaction_residue_5
select interaction_residue_5 , byres ((chain_A within 5.0 of chain_B) + (chain_B within 5.0 of chain_A))

#扩充ligand-5到残基 
select ligand-interaction , byres ligand-5 

#显示侧链，包括CA
show sticks , interaction_residue_5 and (not name n+c+o) 
show sticks , interaction_residue_5 and (resn pro) and (not name c+o) 

#居中放大第120残基
zoom 120/    

#居中放大chain A
zoom A//     

#居中放大chain B的120残基的CA
zoom B/120/CA    

#保存视角为view-1，不保存object的representation
view view-1 , store   

#恢复视角view-1
view view-1 , recall  

#设置chain A 透明度 0.5
set cartoon_transparency , 0.5 , chain A 

#改变complex中chain B为chain C
alter (complex and chain B) , chain = "C" 

#背景颜色white
bg_color white   

#去除溶剂
remove solvent   

#查看color命令的帮助
help color       

#设置chain B的cartoon颜色lightblue
set cartoon_color , lightblue , chain B    

#设置chain B的C原子颜色lightpink
color lightpink , Chain B and symbol C     


# cartoon的helix设置为width 0.1，length 0.7
set cartoon_oval_width , 0.1
set cartoon_oval_length , 0.7

# cartoon的beta sheet设置为width 0.1，length 1.2
set cartoon_rect_width , 0.1
set cartoon_rect_length , 1.2

# spheres的scale设置为0.5
set sphere_scale , 0.5

# ray渲染后，不显示阴影
set ray_shadow , 0

# ray渲染后，用黑线画出cartoon
set ray_trace_mode, 1

# 打开透视效果
set orthoscopic , 1

# png 一个2000*2000图，dpi 300，ray = true（1）
png tmp.png , 2000 , 2000 , 300 , 1

# 设置label小数位数1
set label_digits , 1

# 设置label大小，正数为point size，负数为Angstrom-based size
set label_size , -0.4

# 设置自定义颜色[R,G,B]
set_color color-1 , [255,255,255]

# 添加，取消共价键，先选择两个原子pk1，pk2
bond pk1,pk2
unbond pk1,pk2

# 蛋白二级结构主要通过主链几何结构和氢键模式来确定的，PyMOL默认使用 DSSP 算法分配二级结构类型。可以使用“dss”命令重新计算并显示二级结构，这个命令将生成与 DSSP或其它程序稍有不同的果，大多数差异发生在边界或过渡区域。一般来说，PyMOL 采用算法比较严格，而 dss 是另一种二级结构分配算法。
dss

# 更改一切
#更改链名，将 A 链改为 B 链
alter (chain A),chain='B' 

#更改残基编号，所有残基编号加 100
alter (all),resi=str(int(resi)+100)

# 重启pymol
reinitialize 

# 设置fancy的helix
set cartoon_fancy_helices , 1
set cartoon_dumbbell_length , 0.8
set cartoon_dumbbell_width , 0.1
set cartoon_dumbbell_radius , 0.1

# 设置sticks粗细
set stick_radius , 0.22

# 设置截面
clip near/far, -25

# ray后更好看
set direct , 1    				# 设置直射光为1
set ambient , 0.3 				# 设置环境光为0.3
set ray_opaque_background, 1 	# 背景设置不透明
set ray_shadow , 0   			# ray渲染后，不显示阴影
set ray_trace_mode, 1   		# ray渲染后，用黑线画出轮廓

# surface格式
set surface_mode, 0 			#表面不包含杂原子
set surface_mode, 1 			#所有原子均生成表面，包含 HET 和氢原子
set surface_mode, 3 			#可见对象生成表面
util.ray_shadows('occlusion2') 	#设置阴影，视情况而定可能不太好看
set light_count, 1
set surface_color , lightblue

# stick-ball球棍模型
set stick_ball,1
set stick_radius, 0.12
set stick_ball_ratio, 3

#              ^ Y
#              |
#              |
#              |
#              |----------> X
#             /
#            /
#           /
#          Z

          
# 旋转 chain_A ，绕Y轴 -90 度
rotate y , -90 , chain_A

# 移动 chain_B ，沿X轴 25 A 
translate [25,0,0] , chain_B

# align两个蛋白, super 主要是基于机构进行叠合；align 主要是基于序列进行叠合。
super proteinA , proteinB
super 6r3q and chain B and (resi 31-56 or resi 211-395) , 3sn6 and chain Aand (resi 31-56 or resi 211-395)


#保存蛋白序列
save 1.fasta, 4bhk and chain A and resi 200-210

# 缩略词
organic org. Non-polymer organic compounds (e.g. ligands, buffers)
inorganic ino. Non-polymer inorganic atoms/ions
solvent sol. Water molecules
polymer pol. Protein or Nucleic Acid
polymer.protein Protein (New in PyMOL 2.1)
polymer.nucleic Nucleic Acid (New in PyMOL 2.1)
guide Protein CA and nucleic acid C4*/C4’
hetatm Atoms loaded from PDB HETATM records
hydrogens h. Hydrogen atoms
backbone bb. Polymer backbone atoms (new in PyMOL 1.6.1)
sidechain sc. Polymer non-backbone atoms (new in PyMOL 1.6.1)
metals Metal atoms (new in PyMOL 1.6.1)
donors don. Hydrogen bond donor atoms
acceptors acc. Hydrogen bond acceptor atoms
```

Pymol create electron density map :

```
# 生成6sps的mesh，表面仅在配体原子的 2.4 埃半径内，contour level 0.38
fetch 6sps
fetch 6sps, type=2fofc
isomesh 6sps_mesh , 6sps_2fofc, level = 0.38 , selection = 6sps , carve = 2.4

# 设置mesh格式mesh_as_cylinders 为 0
set mesh_as_cylinders , 0

# 设置mesh格式mesh_width 为 0.8
set mesh_width , 0.8

# 设置mesh格式mesh_color 为 black
set mesh_color , black
```

蛋白的口袋的静电势表面

```
step1. 显示整个蛋白蛋白的静电势表面；A->generate->vacuum electrostatic->potential
step2  设置口袋的中心，一般以其中的配体作为中心；
set surface_carve_selection, ligand
step3  设置口袋的大小
set surface_carve_cutoff, 5
step4 设置口袋的表面的透明度
set transparency,0.3, 1azm_e_chg
step5 切换为溶剂可接触表面
set surface_solvent, 1
```

虚线设置:

```
set cartoon_gap_cutoff, 0
set cartoon_gap_cutoff, 100
```

计算结合表面积**solvent accessible surface** area (SASA)

```
set dot_solvent , 1
get_area (GPR174 within 4.3 of lysoPS) #需要两个object，不能是一个
```

