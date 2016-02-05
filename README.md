# 作業記録
(2016/02/05) メモリリークしている．動作がとても遅い.
(2016/02/05) PySide用テンプレート途中(50%) 
(2016/02/05) MatplotlibApp用テンプレート完成

# FiSimulator
FiSimulatorとはアルゴリズム開発やアルゴリズム検証時に利用するツールである．アルゴリズム開発の本質はアルゴリズムの実装にある．
しかし，実装結果をコマンドラインやcsv出力だけで評価することはセンスがない．アルゴリズム開発には必ずビューアが必要である．
理論(Seory)->計算(Programing)->描魅(View)．
開発者には理論>計算に集中する必要があり描魅にはコストを避けない．
しかし，開発成果は描魅プロセスが重要である．そこで，魅せるまでの軽量フレームワークを作る

## モジュール構成
FiSimulator/
-WebApp/
    - FiSim-Flask/
        - flaskr.py
        - static
        - template
-QtApp/
    - main_app.py
    - FiSim-PySide-mod
        - plotter

-MatplotlibApp/
    - FigPlotter.py
        - alg_man = AlgorithmManager(params)
        - result_datasets = alg_man.get_results()
        
    - result/
-Algorithm/
    - AlgorithmManager.py
        - def set_params():
        
        - 
    - develop_module/(開発するアルゴリズムのモジュール)
        - init
        - develop_module.py
        - default.config

* AlgorithmManagerBaseClass():
    self.params={'fs':fs, 'win_len':win_len, 'sig_data':sig_data}
    def set_function(funk):
    def set_params():
    def calculation():
    
    
  
* ResultDatasetBaseClass():
    self.x
    self.y
    self.title
    self.xlabel
    self.ylabel
    self.xlim
    self.ylim

* 

## 理念
FiSimulatorはモジュールではなくてテンプレート
