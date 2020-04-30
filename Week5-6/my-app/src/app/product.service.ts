import { Injectable } from '@angular/core';
import {products} from './products';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  products = products;
  constructor() { }
  getProducts(): Observable<any[]> {
    return of(this.products);
  }
}
