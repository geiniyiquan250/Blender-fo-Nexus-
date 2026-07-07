# NeXus 问题修改器使用说明

这份文档说明问题修改器（nxQuestion）。它用于在粒子流程中按条件检查每个粒子的状态，再执行设置属性、生成粒子、循环、变量或脚本等逻辑。

## 问题修改器（nxQuestion）

问题修改器（nxQuestion）把“条件判断”和“动作执行”组织成一个分层列表。你可以在同一个修改器里添加问题节点、动作节点、循环节点、变量节点、脚本节点和文件夹节点，用它们组合出逐粒子的逻辑流程。

通常先让场景中已经有可参与计算的粒子，再添加问题修改器（nxQuestion）。它本身不负责产生粒子，而是根据当前粒子数据决定什么时候检查、满足条件后做什么，以及是否继续进入后续节点。

### 设置页（Section）
设置页（Section）用于切换当前显示的主设置页。问题修改器（nxQuestion）除了自己的物体属性（Object Properties）页外，还会带有 Quill 页签，以及组（Groups Affected）、映射（Mapping）和衰减（Falloff）这些通用页签。

### 启用（Enabled）
启用（Enabled）控制问题修改器（nxQuestion）是否参与当前 NeXus 计算。关闭后，这个修改器中的条件和动作都不会执行。

### 视口可见（Visible in Editor）
视口可见（Visible in Editor）控制问题修改器（nxQuestion）在编辑器中的辅助显示是否可见。它不改变逻辑本身，只影响编辑时的可见性。

### 物体属性（Object Properties）
物体属性（Object Properties）是问题修改器（nxQuestion）自身的主设置页。这里包括迭代次数、迭代权重和问题列表等核心逻辑设置。

### 发布视图（Published）
发布视图（Published）用于把问题树编辑界面切换成只显示公开参数的简化界面。

开启后，问题列表和节点结构会先隐藏，界面改为集中显示已经公开的变量参数，以及脚本（Script）节点里可暴露出来的参数。它适合给普通使用者留下少量可调入口，让对方直接改数值，不用进入完整节点树。

### Quill 页签（Quill）
Quill 页签（Quill）用于通过自然语言描述，辅助生成或整理问题树中的节点结构。它适合在你已经明确想要的逻辑行为时，先写一段需求描述，再让 Quill 帮你生成基础结构。

Quill 页签（Quill）当前包括模型选择、对话记录、描述输入、构建按钮、停止按钮和独立窗口入口。如果插件首选项里还没有可用模型，这个页签会提示先到首选项中完成 Quill 配置。

### 模型（Model）
模型（Model）用于选择当前 Quill 页签（Quill）要使用的模型配置。

问题修改器（nxQuestion）会从插件首选项里读取已经配置好的模型列表。这里切换模型后，后续的描述生成会使用当前选中的模型。

### 对话（Conversation）
对话（Conversation）区域显示当前问题修改器（nxQuestion）最近的 Quill 往来记录。

它适合回看刚才输入过的描述，以及 Quill 最近一次构建时的上下文。这个记录会帮助你在多次补充描述时保持连续性。

### 新建对话（New）
新建对话（New）用于清空当前 Quill 会话，重新开始一轮新的描述和构建。

当你准备从头改写一套逻辑，或者不想继续沿用前一轮上下文时，可以先使用这个按钮。

### 行为描述（Prompt）
行为描述（Prompt）输入框用于填写你希望 Quill 生成的行为说明。

这里适合直接写清楚条件、目标和动作，例如希望粒子按邻居距离聚拢、在满足条件时改颜色、或在特定阶段生成新粒子。描述越清楚，生成出来的基础结构通常越接近需求。

### 构建（Build）
构建（Build）按钮用于让 Quill 按当前描述开始生成问题树节点。

点击后，问题修改器（nxQuestion）会进入运行状态，并在界面里显示当前处理进度和构建中的节点摘要。

### 停止（Stop）
停止（Stop）按钮在 Quill 正在运行时出现，用于中断当前生成过程。

当你发现描述需要重写，或者当前生成方向不对时，可以先停止，再修改行为描述（Prompt）重新构建。

### 状态（Status）
状态（Status）用于显示最近一次 Quill 构建的结果、提示或错误信息。

构建完成后，这里会显示成功或失败的简要反馈；构建进行中时，会显示当前进度说明。

### 打开 Quill（Open Quill）
打开 Quill（Open Quill）按钮用于打开独立的 Quill 窗口。

如果你想在更大的界面里继续和 Quill 交互，或查看更完整的构建过程，可以从这里进入独立窗口。

### 迭代次数（Iterations）
迭代次数（Iterations）设置问题修改器在一次更新中重复执行逻辑的次数。数值越高，同一批粒子在一次计算里被连续处理的轮数越多。

### 迭代权重（Iteration Weight）
迭代权重（Iteration Weight）为每一轮迭代提供整体权重。它用于控制重复执行时每轮逻辑的影响强度。

### 问题（Questions）
问题（Questions）列表是问题修改器的主层级列表。这里保存所有问题节点、动作节点、循环节点、变量节点、脚本节点和文件夹节点。

### 当前问题索引（Active Question Index）
当前问题索引（Active Question Index）表示问题列表里当前被选中的条目。通常通过点击列表项切换，而不是手动输入索引。

### 添加菜单（Add Menu）
添加菜单（Add Menu）打开一个类型菜单，用于选择要新增的问题条目类型。你会在这里决定新条目是问题、动作、循环、变量、脚本还是文件夹。

### 添加项（Add Item）
添加项（Add Item）在当前层级中加入一个新条目。对于问题修改器（nxQuestion），新增条目的具体类型由添加菜单（Add Menu）里的选择决定。

### 移除项（Remove Item）
移除项（Remove Item）删除当前选中的条目。对于容器型条目，移除时会连同它的子条目一起移除。

### 上移项（Move Item Up）
上移项（Move Item Up）把当前选中的项在同级顺序中上移一位。它只调整逻辑组织顺序，不改变条目内部参数。

### 下移项（Move Item Down）
下移项（Move Item Down）把当前选中的项在同级顺序中下移一位。用它可以整理执行结构和阅读顺序。

### 增加缩进（Indent Item）
增加缩进（Indent Item）把当前项缩进到前一个容器项下面。它用于把项放进问题、循环或文件夹内部，形成层级结构。

### 减少缩进（Outdent Item）
减少缩进（Outdent Item）把当前项从上一级容器中移出。它用于调整逻辑层级，重新安排项的归属位置。

### 切换启用（Toggle Enabled）
切换启用（Toggle Enabled）控制当前列表项是否参与执行。关闭某个项后，它会保留在结构里，但不会参与当前逻辑。

### 条目名称（Item Name）
条目名称（Item Name）是列表中显示的名称。默认名称会根据条目类型和设置自动生成，手动改名后可用于更清楚地组织复杂逻辑。

### 条目启用（Item Enabled）
条目启用（Item Enabled）控制当前问题条目是否生效。它只影响当前条目本身，不会自动改变其他条目的启用状态。

### 项类型（Item Type）
项类型（Item Type）定义当前条目属于哪一种逻辑节点。问题修改器（nxQuestion）支持问题、动作、循环、变量、脚本和文件夹这几类条目。

### 问题（Question）
问题（Question）节点用于建立 `If`、`Else If` 和 `Else` 分支。它负责决定检查哪一类数据、如何比较，以及满足条件后是否继续执行它下面的子条目。

问题（Question）节点本身是一个容器节点，适合把动作节点、循环节点、变量节点或脚本节点放在它下面。这样可以把“先判断，再执行”的逻辑整理成清晰的层级结构。

### 动作（Action）
动作（Action）节点用于在条件成立后执行具体操作。它可以设置粒子属性、给属性累加数值、生成新粒子、杀死粒子，或者在循环里中断后续迭代。

当你已经明确“满足什么条件”以后，通常就在问题（Question）节点下面添加动作（Action）节点。动作节点本身不负责判断，而是负责真正改动结果。

### 文件夹（Folder）
文件夹（Folder）节点用于整理问题列表的层级结构。它适合把同一类逻辑放进一个可折叠分组里，方便大型逻辑树的阅读和维护。

文件夹（Folder）节点主要承担组织作用。它会保留自己的名称和颜色设置，但不会像问题（Question）节点那样单独提供条件判断，也不会像动作（Action）节点那样直接修改粒子。

### 循环（Loop）
循环（Loop）节点用于重复执行它下面的子条目。它可以按粒子、按邻居、按索引范围或按时间循环来组织重复逻辑。

循环（Loop）节点本身也是容器节点。把问题（Question）节点或动作（Action）节点放在循环下面时，表示这些子条目会在每一次循环迭代中重复检查和执行。

### 变量（Variable）
变量（Variable）节点用于声明一个可在当前问题树里读取或写入的变量。它适合保存中间结果、控制分支复用，或给脚本节点提供可共享的数据入口。

变量（Variable）节点只负责定义变量名称、类型和初始值。真正修改变量内容时，通常还需要配合动作（Action）节点中的变量写入功能。

### 显示在发布视图（Show in Published）
显示在发布视图（Show in Published）用于把当前变量条目加入发布视图（Published）的公开参数列表。

勾选后，这个变量会在发布视图（Published）里显示出来，普通使用者可以直接看到并调整它。没有勾选的变量仍然保留在问题树中，只是不会出现在这个简化界面里。

### 脚本（Script）
脚本（Script）节点用于插入自定义 GLSL 逻辑。它适合处理界面现成参数不方便表达、但又需要在问题流程中执行的高级规则。

脚本（Script）节点本身会保存一段脚本源码，并通过编辑脚本（Edit Script）按钮打开独立编辑器。使用它时，通常要先确认前面的变量（Variable）节点和条件节点已经把脚本需要的数据准备好。

### 已扩展（Expanded）
已扩展（Expanded）控制容器型条目是否在列表中展开显示子条目。它只影响编辑时的层级显示，不改变逻辑结果。

### 条件类型（Condition Type）
条件类型（Condition Type）用于在问题节点里选择 `If`、`Else If` 或 `Else`。它决定当前问题条目在分支结构中的角色。

### 逻辑运算符（Logical Operator）
逻辑运算符（Logical Operator）用于给当前条件附加 `AND`、`OR` 等连接方式。它主要在同一层的条件串联时使用。

### 条件类别（Condition Category）
条件类别（Condition Category）决定当前条件从哪里取值。可选来源包括文档数据、粒子数据和数学值。

### 条件粒子数据（Condition Particle Data）
条件粒子数据（Condition Particle Data）选择要检查的粒子属性，例如年龄、速度、颜色、组、半径、发射器或烟雾等。后续会根据选中的属性显示不同的比较方式。

### 条件向量分量（Condition Vector Component）
条件向量分量（Condition Vector Component）用于从位置、速度、颜色、旋转或 UVW 这类向量数据中选出具体分量。它让条件只检查某个轴或某个颜色通道。

### 条件文档数据（Condition Document Data）
条件文档数据（Condition Document Data）选择场景级别的检查目标，例如当前帧、时间、到摄像机的距离、相机视场或到物体的距离。它用于让粒子逻辑响应场景状态。

### 条件数学数据（Condition Math Data）
条件数学数据（Condition Math Data）选择数学来源，例如常量、随机数、样条、变量或波形。它适合构造不直接依赖单个粒子属性的判断值。

### 条件比较（Condition Comparison）
条件比较（Condition Comparison）指定比较方式，例如小于、等于、大于或区间内。它决定当前条件如何解释下面输入的比较值。

### 条件包含关系（Condition Inclusion）
条件包含关系（Condition Inclusion）用于组、发射器、计数或 ID 这类离散值的包含判断。它决定当前值要“在集合内”还是“在集合外”才算满足条件。

### 条件数值（Condition Value）
条件数值（Condition Value）是当前条件使用的基础比较值。对于浮点类属性，它表示与粒子数据、文档数据或数学值直接比较的目标数值。

### 条件数值变化（Condition Value Variation）
条件数值变化（Condition Value Variation）为条件数值（Condition Value）增加变化范围。它用于让判断阈值不是完全固定的单一数值。

### 条件上限（Condition To）
条件上限（Condition To）在“区间内”或“区间外”比较时定义上边界。它与条件数值（Condition Value）一起形成一个判断范围。

### 条件整数值（Condition Integer Value）
条件整数值（Condition Integer Value）用于整数类条件的基础比较值，例如组编号、粒子计数或粒子 ID。它只在当前数据类型使用整数比较时出现。

### 条件整数变化（Condition Integer Variation）
条件整数变化（Condition Integer Variation）为条件整数值（Condition Integer Value）添加变化范围。它用于整数条件的随机或浮动阈值。

### 条件整数上限（Condition Integer To）
条件整数上限（Condition Integer To）用于整数区间比较时的上边界。只有比较方式需要范围时才会出现。

### 条件时间（Condition Time）
条件时间（Condition Time）用于时间类条件的基础比较值。它适合用在年龄、寿命或文档时间这类以时间表达的数据上。

### 条件时间变化（Condition Time Variation）
条件时间变化（Condition Time Variation）为条件时间（Condition Time）加入变化范围。它用于让时间阈值带有浮动。

### 条件时间上限（Condition Time To）
条件时间上限（Condition Time To）是时间区间判断时的上边界。只有使用区间比较时才显示。

### 数学常量值（Math Constant Value）
数学常量值（Math Constant Value）给数学条件中的常量模式提供固定输入值。选择常量来源时，当前条件就直接使用这里的数值。

### 数学频率（Math Frequency）
数学频率（Math Frequency）控制波形数学源的变化频率。它影响波形值随时间或粒子索引变化的快慢。

### 数学时间变化（Math Time Variation）
数学时间变化（Math Time Variation）指定波形数学源如何依赖时间。你可以让它不依赖时间，或跟随文档时间、粒子时间变化。

### 数学粒子 ID（Math Particle ID）
数学粒子 ID（Math Particle ID）决定数学值是否把粒子索引作为输入之一。启用后，不同粒子更容易得到不同的波形或数学结果。

### 数学变量名（Math Variable Name）
数学变量名（Math Variable Name）指定数学条件在变量模式下要读取哪个变量。它应当对应当前逻辑里已经声明并可访问的变量名称。

### 数学随机最小值（Math Random Min）
数学随机最小值（Math Random Min）设置随机条件值的下限。随机模式会在这个下限和上限之间生成结果。

### 数学随机最大值（Math Random Max）
数学随机最大值（Math Random Max）设置随机条件值的上限。它与数学随机最小值（Math Random Min）一起限定随机区间。

### 数学随机种子（Math Random Seed）
数学随机种子（Math Random Seed）控制随机值的分布结果。修改它可以在不改变区间的前提下得到不同的随机序列。

### 邻居距离（Neighbor Distance）
邻居距离（Neighbor Distance）用于粒子邻居条件的搜索半径。只有落在这个距离范围内的邻居才会参与相关判断。

### 检查一次（Check Once）
仅检查一次（Check Once）让当前条件只在每个粒子身上判断一次。适合需要“命中一次后不再重复检查”的逻辑。

### 对象距离模式（Object Distance Mode）
对象距离模式（Object Distance Mode）决定“到物体的距离”如何测量。可用模式包括按对象位置、点、面或体积来解释距离。

### 条件相机（Condition Camera）
条件相机（Condition Camera）指定要参考的相机对象。它在相机距离或相机场景视场条件中使用。

### 加宽FOV（Widen FOV）
加宽FOV（Widen FOV）为相机视场判断增加额外角度。它可以把原本的相机可视范围向外放宽。

### 条件对象列表（Condition Objects）
条件对象列表（Condition Objects）列出“到物体的距离”条件使用的目标对象。只有这里的对象会参与距离判断。

### 活动对象索引（Active Object Index）
活动对象索引（Active Object Index）表示条件对象列表里当前被选中的条目。它用于确定当前正在编辑哪一个对象引用。

### 添加对象（Add Object）
添加对象（Add Object）把一个对象加入条件对象列表。之后该对象会参与对象距离相关的条件检查。

### 条件发射器列表（Condition Emitters）
条件发射器列表（Condition Emitters）列出当前条件允许检查的发射器对象。它用于基于发射器来源来判断粒子是否匹配。

### 当前发射器索引（Active Emitter Index）
当前发射器索引（Active Emitter Index）表示条件发射器列表里当前选中的条目。它只用于编辑当前引用，不直接改变逻辑意义。

### 添加发射器（Add Emitter）
添加发射器（Add Emitter）把一个发射器对象加入条件发射器列表。只有这里列出的发射器才会用于当前发射器条件。

### 引用对象（Referenced Object）
引用对象（Referenced Object）是条件对象列表或条件发射器列表中某个条目实际引用的目标。它会根据当前列表的用途，指向普通对象或发射器对象。

### 引用启用（Reference Enabled）
引用启用（Reference Enabled）控制当前引用条目是否参与条件判断。关闭后，该引用会保留在列表里，但不会被用于匹配。

### 击中对象（Hit Object）
击中对象（Hit Object）用于检查粒子是否发生过对象碰撞。它属于粒子标记条件的一部分。

### 击中粒子（Hit Particle）
击中粒子（Hit Particle）用于检查粒子是否与其他粒子碰撞。只有使用标记条件时才会显示。

### 改变的组（Changed Group）
改变的组（Changed Group）用于检查粒子是否已经被切换到其他组。它适合配合分组流程做后续逻辑分支。

### 卡住（Stuck）
卡住（Stuck）用于检查粒子是否处于卡住状态。它属于粒子标记条件中的布尔检查。

### 已已冻结（Frozen）
已冻结（Frozen）用于检查粒子是否被冻结。它适合后续对冻结粒子执行额外处理或跳过某些动作。

### 出生（Born）
出生（Born）用于检查粒子是否刚刚出生。它常用于只在粒子初始阶段触发的逻辑。

### 条目权重（Item Weight）
条目权重（Item Weight）控制当前问题节点或动作节点的影响权重。它用于调节单个逻辑条目在整体结果中的强弱。

### 动作类型（Action Type）
动作类型（Action Type）决定动作节点要执行什么操作。可用类型包括设置、累加、生成粒子、杀死粒子和中断循环。

### 动作属性（Action Property）
动作属性（Action Property）指定 `Set` 或 `Add` 操作要作用到哪种粒子属性。不同属性会显示不同的输入字段。

### 动作颜色（Action Color）
动作颜色（Action Color）用于把颜色写入粒子。它在目标属性选择颜色时出现。

### 动作颜色变化（Action Color Variation）
动作颜色变化（Action Color Variation）为动作颜色（Action Color）增加随机变化。它适合让写入的颜色不是完全一致。

### 动作数值（Action Numeric Value）
动作数值（Action Numeric Value）用于速度、质量或半径这类数值属性的写入值。具体作用由当前动作属性（Action Property）决定。

### 动作数值变化（Action Numeric Variation）
动作数值变化（Action Numeric Variation）为动作数值（Action Numeric Value）提供变化范围。它让同一动作作用到不同粒子时产生差异。

### 动作寿命（Action Life）
动作寿命（Action Life）用于写入粒子的寿命。它只在目标属性是寿命时出现。

### 动作寿命变化（Action Life Variation）
动作寿命变化（Action Life Variation）为动作寿命（Action Life）增加变化范围。这样写入的寿命可以带有浮动。

### 动作年龄（Action Age）
动作年龄（Action Age）用于写入粒子的年龄。它适合重置、偏移或直接设置粒子年龄。

### 动作年龄变化（Action Age Variation）
动作年龄变化（Action Age Variation）为动作年龄（Action Age）提供变化范围。它只在设置年龄时使用。

### 动作缩放（Action Scale）
动作缩放（Action Scale）写入粒子的缩放向量。它适用于需要直接调整粒子尺寸或比例的逻辑。

### 动作缩放变化（Action Scale Variation）
动作缩放变化（Action Scale Variation）为动作缩放（Action Scale）增加随机波动。它让写入的缩放不完全一致。

### 动作旋转（Action Rotation）
动作旋转（Action Rotation）用于写入粒子的旋转值。它接受一个三轴旋转向量。

### 动作旋转变化（Action Rotation Variation）
动作旋转变化（Action Rotation Variation）为动作旋转（Action Rotation）增加变化范围。适合给旋转加入随机扰动。

### 动作速度（Action Velocity）
动作速度（Action Velocity）用于写入粒子速度向量。它适合直接覆盖或累加三维运动方向。

### 动作速度变化（Action Velocity Variation）
动作速度变化（Action Velocity Variation）为动作速度（Action Velocity）添加向量变化。它适合生成更自然的不规则速度结果。

### 动作组（Action Group）
动作组（Action Group）指定要把粒子切换到哪个组对象。这个字段只接受 `nxGroup` 对象。

### 动作变量（Action Variable）
动作变量（Action Variable）指定要写入的变量名称。它用于把当前动作作用到某个变量，而不是直接作用到粒子物理属性。

### 变量赋值来源（Variable Assignment Source）
变量赋值来源（Variable Assignment Source）决定变量写入的是常量，还是当前问题计算出的值。它只在变量动作中出现。

### 动作变量值（Action Variable Value）
动作变量值（Action Variable Value）是变量动作在常量模式下写入的数值。只有赋值来源为常量时，这个数值才是最终写入内容。

### 冻结状态（Freeze State）
冻结状态（Freeze State）用于把粒子冻结状态写为开或关。它只在目标属性是冻结时出现。

### 粘附状态（Sticky State）
粘附状态（Sticky State）用于把粒子粘附状态写为开或关。它只在目标属性是粘附时出现。

### 动作延迟（Action Delay）
动作延迟（Action Delay）为当前动作加入一个延迟比例。它适合让设置或累加效果不是立刻完全生效。

### 动作阻尼（Action Damping）
动作阻尼（Action Damping）控制动作延迟后的衰减或缓和程度。它和动作延迟（Action Delay）一起影响动作变化过程。

### 设置一次（Set Once）
仅设置一次（Set Once）限制当前动作对每个粒子只执行一次。它适合只需首次命中时生效的设置操作。

### 动作显示（Action Display）
动作显示（Action Display）用于把粒子的显示模式写成指定样式，例如点、线、圆或球体。它只在动作属性为显示时出现。

### 生成数量（Spawn Count）
生成数量（Spawn Count）设置一次动作要生成多少新粒子。它只在动作类型是生成粒子时出现。

### 生成距离（Spawn Distance）
生成距离（Spawn Distance）控制新粒子与来源位置之间的偏移距离。它用于决定生成粒子的起始分布范围。

### 生成颜色（Spawn Color）
生成颜色（Spawn Color）指定新生成粒子的颜色。它在不完全继承父粒子属性时尤其有用。

### 完整寿命（Full Life）
完整寿命（Full Life）控制新粒子是否使用完整寿命。关闭后，才会继续显示单独的生成寿命（Spawn Life）设置。

### 生成寿命（Spawn Life）
生成寿命（Spawn Life）设置新生成粒子的寿命。只有在不使用完整寿命时才会启用这个字段。

### 速度方向（Velocity Direction）
速度方向（Velocity Direction）决定新生成粒子的初始速度方向是随机，还是继承源方向。它只在生成动作中出现。

### 生成速度（Spawn Speed）
生成速度（Spawn Speed）设置新生成粒子的初始速度大小。它和速度方向（Velocity Direction）一起决定最终初速。

### 生成半径（Spawn Radius）
生成半径（Spawn Radius）设置新生成粒子的半径。启用继承父级后，这个字段可能不再单独起作用。

### 继承父级（Inherit Parent）
继承父级（Inherit Parent）让新粒子尽量继承父粒子的属性。启用后，一部分单独的生成属性会被关闭或改为继承来源。

### 生成发射器（Spawn Emitter）
生成发射器（Spawn Emitter）指定生成动作使用哪个发射器对象作为来源。只有有效的 `nxEmitter` 对象能被选中。

### 循环类型（Loop Type）
循环类型（Loop Type）决定循环节点按什么方式重复。可用方式包括逐项遍历、索引循环和时间循环。

### 循环名称（Loop Name）
循环名称（Loop Name）用于给当前循环命名。这个名字主要帮助你在复杂结构中识别循环用途。

### 对每个（For Each）
对每个（For Each）定义逐项遍历时要遍历的是粒子还是邻居。它只在循环类型为逐项遍历时显示。

### 邻居搜索距离（Neighbor Search Distance）
邻居搜索距离（Neighbor Search Distance）为邻居遍历提供搜索半径。只有在逐邻居循环时，这个距离才会被使用。

### 循环起点（Loop Start）
循环起点（Loop Start）设置索引循环的起始值。它只在索引循环模式下出现。

### 循环终点（Loop End）
循环终点（Loop End）设置索引循环的结束值。它与循环起点（Loop Start）和循环步长（Loop Step）共同决定范围。

### 循环步长（Loop Step）
循环步长（Loop Step）定义索引循环每次前进多少。它只在索引循环模式下出现。

### 开始时间（Start Time）
开始时间（Start Time）设置时间循环的起始时间。它只在时间循环模式下使用。

### 持续时间（Duration）
持续时间（Duration）定义一次时间循环覆盖多长时间。它配合开始时间（Start Time）决定单个时间段长度。

### 循环次数（Cycle Count）
循环次数（Cycle Count）设置时间循环重复多少次。数值越高，时间采样会重复更多轮。

### 时间来自（Time From）
时间来自（Time From）决定时间循环使用文档时间还是粒子时间。它影响时间循环对场景和粒子状态的响应方式。

### 插值位置（Interpolate Position）
插值位置（Interpolate Position）控制时间循环是否重建位置通道。它只在时间循环模式下出现。

### 插值速度（Interpolate Velocity）
插值速度（Interpolate Velocity）控制时间循环是否重建速度通道。启用后，循环会把速度也纳入时间变化。

### 插值半径（Interpolate Radius）
插值半径（Interpolate Radius）控制时间循环是否重建半径通道。它适合处理粒子尺寸随时间变化的循环。

### 插值颜色（Interpolate Color）
插值颜色（Interpolate Color）控制时间循环是否重建颜色通道。启用后，循环可让颜色随时间重复。

### 插值质量（Interpolate Mass）
插值质量（Interpolate Mass）控制时间循环是否重建质量通道。它只在时间循环模式下出现。

### 插值旋转（Interpolate Rotation）
插值旋转（Interpolate Rotation）控制时间循环是否重建旋转通道。它适合对姿态变化做时间重复。

### 声明变量名（Declared Variable Name）
声明变量名（Declared Variable Name）是变量节点创建的变量名称。后续问题节点、动作节点或脚本节点可以通过这个名字引用它。

### 变量类型（Variable Type）
变量类型（Variable Type）决定变量保存的是整数、浮点数、向量还是用户数据。它也决定下面会显示哪一种初始值输入。

### 可写（Writeable）
可写（Writeable）控制这个变量是否允许后续动作写入。关闭时，它更适合作为只读参考值使用。

### 粒子变量（Particle Variable）
粒子变量（Particle Variable）决定变量是每个粒子各自保存，还是作为更通用的共享逻辑变量使用。启用后，不同粒子可以拥有不同变量值。

### 整数初始值（Integer Initial Value）
整数初始值（Integer Initial Value）是整数变量的默认起始内容。只有变量类型为整数时才会显示。

### 浮点初始值（Float Initial Value）
浮点初始值（Float Initial Value）是浮点变量的默认起始内容。只有变量类型为浮点时才会显示。

### 向量初始值（Vector Initial Value）
向量初始值（Vector Initial Value）是向量变量的默认三维值。只有变量类型为向量时才会显示。

### 编辑脚本（Edit Script）
编辑脚本（Edit Script）打开当前脚本节点的 GLSL 编辑器。你可以在外部脚本窗口中编写、修改并保存这个节点的源码。

### 文件夹设置（Folder Settings）
文件夹设置（Folder Settings）打开文件夹节点的小型设置面板。这里主要用于修改文件夹名称和列表显示颜色。

### 文件夹颜色（Folder Color）
文件夹颜色（Folder Color）用于给文件夹节点设置列表颜色。它只影响列表中的组织显示，不参与粒子计算。

### 组（Groups Affected）
组（Groups Affected）列出哪些粒子组会受到当前问题修改器（nxQuestion）影响。列表为空时，表示不按组限制。

### 活动组索引（Active Group Index）
活动组索引（Active Group Index）表示组列表里当前被选中的条目。通常通过点击列表项切换。

### 添加组（Add Group）
添加组（Add Group）向组列表加入一个新的组引用。之后当前修改器只会作用于这些被列出的组。

### 组对象（Group Object）
组对象（Group Object）指定某个组条目实际引用的 `nxGroup` 对象。只有匹配这些组的粒子会进入当前修改器逻辑。

### 组启用（Group Enabled）
组启用（Group Enabled）控制某个组条目是否参与过滤。关闭后，该条目会保留但暂时不生效。

### 映射（Mapping）
映射（Mapping）用于让粒子数据驱动当前修改器里的参数。它不直接增加一个新逻辑节点，而是给参数提供动态控制来源。

### 映射层（Mapping Layers）
映射层（Mapping Layers）是当前修改器的映射条目列表。每一层都描述一个“用什么粒子数据去驱动哪个参数”的关系。

### 活动映射索引（Active Mapping Index）
活动映射索引（Active Mapping Index）表示映射层列表里当前被选中的条目。它决定下面正在编辑哪一层映射。

### 映射参数（Mapping Parameter）
映射参数（Mapping Parameter）指定当前映射要驱动哪个参数。只有被选中的参数会接受这层映射输入。

### 映射源数据（Mapping Source Data）
映射源数据（Mapping Source Data）指定这层映射从哪种粒子数据读取输入。它决定驱动值来自速度、年龄、颜色还是其他粒子属性。

### 映射层 ID（Mapping Layer）
映射层 ID（Mapping Layer）用于区分和组织多层映射。它帮助多个映射同时存在时保持层级关系清晰。

### 范围最小值（Range Min）
范围最小值（Range Min）定义映射输入范围的下限。粒子数据低于这个值时，会按映射规则落到下边界附近。

### 范围最大值（Range Max）
范围最大值（Range Max）定义映射输入范围的上限。它与范围最小值（Range Min）一起限定映射区间。

### 映射权重（Mapping Weight）
映射权重（Mapping Weight）控制当前映射层的影响强度。它用于调节映射结果作用到目标参数上的程度。

### 钳制（Clamp）
钳制（Clamp）决定映射结果是否限制在设定范围内。启用后，超出范围的输入不会继续向外扩张。

### 映射启用（Mapping Enabled）
映射启用（Mapping Enabled）控制当前映射层是否参与计算。关闭后，这一层映射会保留，但不会驱动参数。

### 衰减（Falloff）
衰减（Falloff）用于按空间对象或场的影响范围限制当前修改器。它适合把逻辑效果限制在特定区域内。

### 衰减对象（Falloff Objects）
衰减对象（Falloff Objects）是当前修改器使用的衰减对象列表。只有这些对象定义的衰减范围会参与计算。

### 活动衰减索引（Active Falloff Index）
活动衰减索引（Active Falloff Index）表示衰减对象列表里当前被选中的条目。它用于切换当前正在编辑的衰减对象。

### 添加衰减（Add Falloff）
添加衰减（Add Falloff）向衰减对象列表中加入一个新的衰减引用。加入后，这个对象的场效应就可以参与限制当前修改器。

### 衰减对象（Falloff Object）
衰减对象（Falloff Object）指定某个衰减条目实际引用的对象。当前修改器会根据这个对象提供的衰减范围计算影响。

### 衰减启用（Falloff Enabled）
衰减启用（Falloff Enabled）控制某个衰减条目是否参与计算。关闭后，该衰减对象会保留在列表里，但不再生效。

### 衰减混合（Falloff Blend）
衰减混合（Falloff Blend）定义多个衰减结果如何与当前修改器效果混合。它决定衰减是在加强、削弱还是替换当前作用。

### 衰减混合强度（Falloff Blend Strength）
衰减混合强度（Falloff Blend Strength）控制衰减混合结果的强弱。数值越高，衰减对象对最终效果的调制越明显。
