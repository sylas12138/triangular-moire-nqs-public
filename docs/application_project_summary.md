# 三角格子 t-V / moire pinball 项目经历

该项目围绕三角格子 spinless fermion 的 charge ordering、generalized Wigner crystal 和 moire pinball-like 候选态展开。它不是单纯复现一个模型，而是训练我如何从 ED benchmark 出发，判断 NQS/VMC 是否值得放大到更复杂体系。

第一条线是 `nu=1/3` triangular nearest-neighbor `t-V` benchmark。该体系在强相互作用下倾向于三子晶格电荷有序，是检验 NQS ansatz、sampler、branch locking 和 replay stability 的好平台。项目中我关注的不只是训练最低能量，而是 train-best 与 strict replay 是否一致，branch/sector 是否稳定，以及 ansatz 是否真正改善了 charge-order sector 的表达。

第二条线是 `nu=2/3` triangular moire extended Hubbard `t-V1-V2-V3` benchmark。该方向通过 ED 扫描寻找 `S_c(K)` 增强但动能仍保留的中间窗口，用于描述 pinball-like partially itinerant charge-order candidate。项目诊断包括 charge structure factor、三子晶格密度不均匀度、charge gap、neutral spectrum、bond-resolved kinetic、twist/boundary audit 和 shape check。当前更稳妥的结论是 finite-cluster ridge candidate，而不是直接宣称热力学 pinball phase。

这个项目让我意识到，NQS/AI4S 在强关联体系中的价值不只是扩大模型尺寸，也包括建立“先 benchmark、再放大”的科学流程：先用 ED 和机制诊断确定候选窗口，再决定 NQS/VMC 是否能提供新的可计算信息。

