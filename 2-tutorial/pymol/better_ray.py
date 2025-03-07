cmd.bg_color("white")  # 设置背景颜色为白色

# 去除溶剂
cmd.remove("solvent")

# cartoon 的 helix 设置
cmd.set("cartoon_oval_width", 0.1)
cmd.set("cartoon_oval_length", 0.7)

# cartoon 的 beta sheet 设置
cmd.set("cartoon_rect_width", 0.1)
cmd.set("cartoon_rect_length", 1.2)

# spheres 的 scale 设置
cmd.set("sphere_scale", 0.5)

# ray 渲染后，不显示阴影
cmd.set("ray_shadow", 0)

# ray 渲染后，用黑线画出 cartoon
cmd.set("ray_trace_mode", 1)

# 打开透视效果
cmd.set("orthoscopic", 1)

# ray 渲染优化
cmd.set("direct", 1)  # 设置直射光
cmd.set("ambient", 0.3)  # 设置环境光
cmd.set("ray_opaque_background", 1)  # 背景设置不透明
cmd.set("ray_shadow", 0)  # 再次设置 ray 渲染无阴影
cmd.set("ray_trace_mode", 1)  # 再次强调轮廓线
