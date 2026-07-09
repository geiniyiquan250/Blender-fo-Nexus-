# NeXus 中文帮助文档（更新时间2026.7.7）（补充：目前文档的状态不够直白直观和缺少因果关系帮助理解，我仍在考虑重新编写，以让整个帮助文档更加符合“帮助文档”）

这个仓库整理的是 Blender 用 NeXus 插件的中文帮助文档。

这里的帮助内容已经按独立 Markdown 文档整理，普通用户可以直接在 GitHub 里按名称浏览、搜索和跳转。

文档索引：

- 吸引修改器（nxAttract）：[nxAttract.md](./nxAttract.md)
- 避让修改器（nxAvoid）：[nxAvoid.md](./nxAvoid.md)
- 混合修改器（nxBlend）：[nxBlend.md](./nxBlend.md)
- nx 缓存（nxCache）：[nxCache.md](./nxCache.md)
- 碰撞体修改器（nxCollider）：[nxCollider.md](./nxCollider.md)
- 颜色修改器（nxColor）：[nxColor.md](./nxColor.md)
- 约束修改器（nxConstraints）：[nxConstraints.md](./nxConstraints.md)
- 覆盖修改器（nxCover）：[nxCover.md](./nxCover.md)
- 树枝生长修改器（nxDendrite）：[nxDendrite.md](./nxDendrite.md)
- 方向修改器（nxDirection）：[nxDirection.md](./nxDirection.md)
- 阻力修改器（nxDrag）：[nxDrag.md](./nxDrag.md)
- 发射器（nxEmitter）：[nxEmitter.md](./nxEmitter.md)
- 爆炸修改器（nxExplode）：[nxExplode.md](./nxExplode.md)
- 爆炸特效修改器（nxExplosiaFX）：[nxExplosiaFX.md](./nxExplosiaFX.md)
- nx 衰减（nxFalloff）：[nxFalloff.md](./nxFalloff.md)
- 群聚修改器（nxFlock）：[nxFlock.md](./nxFlock.md)
- 流场修改器（nxFlowField）：[nxFlowField.md](./nxFlowField.md)
- 流体修改器（nxFluids）：[nxFluids.md](./nxFluids.md)
- 泡沫修改器（nxFoam）：[nxFoam.md](./nxFoam.md)
- 文件夹（nxFolder）：[nxFolder.md](./nxFolder.md)
- 跟随几何体修改器（nxFollowGeo）：[nxFollowGeo.md](./nxFollowGeo.md)
- 生成器修改器（nxGenerator）：[nxGenerator.md](./nxGenerator.md)
- 重力修改器（nxGravity）：[nxGravity.md](./nxGravity.md)
- nx 组（nxGroup）：[nxGroup.md](./nxGroup.md)
- 感染修改器（nxInfectio）：[nxInfectio.md](./nxInfectio.md)
- 销毁修改器（nxKill）：[nxKill.md](./nxKill.md)
- 限制修改器（nxLimit）：[nxLimit.md](./nxLimit.md)
- 网格化修改器（nxMesher）：[nxMesher.md](./nxMesher.md)
- 粒子间碰撞修改器（nxPPCollisions）：[nxPPCollisions.md](./nxPPCollisions.md)
- 推力修改器（nxPush）：[nxPush.md](./nxPush.md)
- 问题修改器（nxQuestion）：[nxQuestion.md](./nxQuestion.md)
- 旋转修改器（nxRotate）：[nxRotate.md](./nxRotate.md)
- 缩放修改器（nxScale）：[nxScale.md](./nxScale.md)
- 薄膜补粒修改器（nxSheeter）：[nxSheeter.md](./nxSheeter.md)
- 速度修改器（nxSpeed）：[nxSpeed.md](./nxSpeed.md)
- 自旋修改器（nxSpin）：[nxSpin.md](./nxSpin.md)
- 飞溅修改器（nxSplash）：[nxSplash.md](./nxSplash.md)
- 粘性修改器（nxSticky）：[nxSticky.md](./nxSticky.md)
- 拖尾修改器（nxTrail）：[nxTrail.md](./nxTrail.md)
- 湍流修改器（nxTurbulence）：[nxTurbulence.md](./nxTurbulence.md)
- 提升分辨率修改器（nxUpres）：[nxUpres.md](./nxUpres.md)
- 涡量修改器（nxVorticity）：[nxVorticity.md](./nxVorticity.md)
- 波浪修改器（nxWave）：[nxWave.md](./nxWave.md)
- 风力修改器（nxWind）：[nxWind.md](./nxWind.md)

目录说明：

- `nx*.md`：面向用户的中文帮助文档。
- `README.md`：仓库简介和文档索引。
- `operators/modifier_help.py`：本地帮助窗口里使用的帮助入口代码。
- `operators/__init__.py`：帮助入口注册代码。
- `build_unified_chinese_injector.py`：维护用打包脚本。
- `check_doc_terms.py`：维护用术语检查脚本。

这个仓库当前以 Markdown 帮助文档为主，也保留了少量仍在使用的帮助接入和维护文件。
