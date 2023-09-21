from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from store.forms import VisitForm, TradeForm, TerritoryForm, SkuForm
from store.models import Trade, Sku, Visit, Territory


def index(request):
    skus = Sku.objects.all()
    visit = Visit.objects.all()
    active = Sku.objects.all()
    sku_id = request.GET.get('Sku')
    form = VisitForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        trade = request.POST.get('trade')
        comment =request.POST.get('comment')
        territory = request.POST.get('territory')
        user = request.user.id
        sku_names = [x.sku_name for x in Sku.objects.all()]
        sku_ids = []
        for x in sku_names:
            sku_ids.append(int(request.POST.get(x))) if request.POST.get(x) else print('0')
        print(sku_ids)
        visit = Visit.objects.create(
            trade_id=trade,
            territory_id=territory,
            user_id=user,
            comment=comment,
        )
        for x in sku_ids:
            visit.sku.add(Sku.objects.get(id=x))
        return redirect('store:home')

    return render(request, 'home.html', {
        'visit': visit,
        'skus': skus,
        'form': form
    })


@login_required(login_url='/users/sign-in')
def create_trade(request):
    trade_form = TradeForm(request.POST or None, request.FILES or None)
    if trade_form.is_valid():
        trade_form.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_trade.html', {
        'trade_form': trade_form
    })


@login_required(login_url='/users/sign-in')
def create_territory(request):
    territory_form = TerritoryForm(request.POST or None, request.FILES or None)
    if territory_form.is_valid():
        territory_form.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_territory.html', {
        'territory_form': territory_form,
    })


@login_required(login_url='/users/sign-in')
def create_sku(request):
    sku_form = SkuForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and sku_form.is_valid():
        instance = sku_form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/create_sku.html', {
        'sku_form': sku_form
    })


@login_required(login_url='/users/sign-in')
def edit_sku(request, pk):
    sku = get_object_or_404(Sku, pk=pk)
    form = SkuForm(request.POST or None, request.FILES or None, instance=sku)
    if form.is_valid():
        form.save()
        return redirect('store:home')
    return render(request, 'create_and_edit_items/edit_page.html', {
        'form': form
    })


def del_sku(request, pk):
    author = Sku.objects.get(pk=pk).delete()
    return redirect('store:home')