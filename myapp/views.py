from django.views.generic import ListView
from .models import Kind, Food


class FoodListView(ListView):
    model = Food

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)

        # 絞り込み条件の設定
        kinds = Kind.objects.all()
        context['kinds'] = kinds
        
        return context
        
        
    def get_queryset(self):
        # デフォルトは全件取得
        results = self.model.objects.all()

        # GETのURLクエリパラメータを取得する
        # 該当のクエリパラメータが存在しない場合は、[]が返ってくる
        q_kinds = self.request.GET.getlist('kind')
        q_name = self.request.GET.get('name')

        # 品種での絞込は、Kind.pkとして存在してる値のみ対象とする
        # "a"とかを指定するとValueErrorになるため
        if len(q_kinds) != 0:
            kinds = [x for x in q_kinds if x in ["1", "2"]]
            results = results.filter(kind__in=kinds)
        
        # 名前での絞り込み
        if q_name is not None:
            results = results.filter(name__contains=q_name)
            
        return results