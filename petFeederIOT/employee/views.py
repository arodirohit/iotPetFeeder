from django.shortcuts import render,redirect
from employee.forms import VoiceCommandForm,BowlWeightForm,FoodContainerWeightForm,FoodLevelMonitorForm
from employee.models import VoiceCommand,BowlWeight,FoodContainerWeight,FoodLevelMonitor

# Create your views here.
def command(request):
    if request.method == "POST":
        form = VoiceCommandForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showCmd')
            except:
                return redirect('/showError')
    else:
        form = VoiceCommandForm()
    return render(request,'indexCmd.html',{'form':form})

def showError(request):
    return render(request,"error.html")

def showCmd(request):
    commands = VoiceCommand.objects.all()
    return render(request,"showCmd.html",{'commands':commands})
def editCmd(request, id):
    command = VoiceCommand.objects.get(id=id)
    return render(request,'editCmd.html', {'command':command})
def updateCmd(request, id):
    command = VoiceCommand.objects.get(id=id)
    form = VoiceCommandForm(request.POST, instance = command)
    if form.is_valid():
        form.save()
        return redirect("/showCmd")
    return render(request, 'editCmd.html', {'command':command})
def destroyCmd(request, id):
    command = VoiceCommand.objects.get(id=id)
    command.delete()
    return redirect("/showCmd")

#BowlWeight Views
def bowlweight(request):
    if request.method == "POST":
        form = BowlWeightForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showBowlWght')
            except:
                return redirect('/showError')
    else:
        form = BowlWeightForm()
    return render(request,'indexBowlWght.html',{'form':form})

def showBowlWght(request):
    bowlweights = BowlWeight.objects.all()
    return render(request,"showBowlWght.html",{'bowlweights':bowlweights})
def editBowlWght(request, id):
    bowlweight = BowlWeight.objects.get(id=id)
    return render(request,'editBowlWght.html', {'bowlWeight':bowlweight})
def updateBowlWght(request, id):
    bowlweight = BowlWeight.objects.get(id=id)
    form = BowlWeightForm(request.POST, instance = bowlweight)
    if form.is_valid():
        form.save()
        return redirect("/showBowlWght")
    return render(request, 'editBowlWght.html', {'bowlWeight':bowlweight})
def destroyBowlWght(request, id):
    bowlweight = BowlWeight.objects.get(id=id)
    bowlweight.delete()
    return redirect("/showBowlWght")

#For Container Weight
def containerWeight(request):
    if request.method == "POST":
        form = FoodContainerWeightForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showContainerWght')
            except:
                return redirect('/showError')
    else:
        form = FoodContainerWeightForm()
    return render(request,'indexContainerWght.html',{'form':form})

def showContainerWght(request):
    containerweights = FoodContainerWeight.objects.all()
    return render(request,"showContainerWght.html",{'containerweights':containerweights})
def editContainerWght(request, id):
    containerweight = FoodContainerWeight.objects.get(id=id)
    return render(request,'editContainerWght.html', {'containerWeight':containerweight})
def updateContainerWght(request, id):
    containerweight = FoodContainerWeight.objects.get(id=id)
    form = FoodContainerWeightForm(request.POST, instance = containerweight)
    if form.is_valid():
        form.save()
        return redirect("/showContainerWght")
    return render(request, 'editContainerWght.html', {'containerWeight':containerweight})
def destroyContainerWght(request, id):
    containerweight = FoodContainerWeight.objects.get(id=id)
    containerweight.delete()
    return redirect("/showContainerWght")

#for IR Sensor
def foodLevelIR(request):
    if request.method == "POST":
        form = FoodLevelMonitorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/showFoodLevel')
            except:
                return redirect('/showError')
    else:
        form = FoodLevelMonitorForm()
    return render(request,'indexFoodLevel.html',{'form':form})

def showFoodLevel(request):
    foodlevels = FoodLevelMonitor.objects.all()
    return render(request,"showFoodLevel.html",{'foodlevels':foodlevels})
def editFoodLevel(request, id):
    foodLevel = FoodLevelMonitor.objects.get(id=id)
    return render(request,'editFoodLevel.html', {'foodLevel':foodLevel})
def updateFoodLevel(request, id):
    foodLevel = FoodLevelMonitor.objects.get(id=id)
    form = FoodLevelMonitorForm(request.POST, instance = foodLevel)
    if form.is_valid():
        form.save()
        return redirect("/showFoodLevel")
    return render(request, 'editFoodLevel.html', {'foodLevel':foodLevel})
def destroyFoodLevel(request, id):
    foodLevel = FoodLevelMonitor.objects.get(id=id)
    foodLevel.delete()
    return redirect("/showFoodLevel")
