var BubbleSort(int a[]){
	int i,j;
	for(i=MAXLENGTH; --i>==0){
		swapped = 0;
		for(j=0; j<i; j++){
			if (a[j] > a[j+1]){
				swap(a[j], a[j+1]);
				swapped = 1;
			}
		}
		if(!swapped) return;
	}
}