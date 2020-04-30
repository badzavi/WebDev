import { Injectable } from '@angular/core';
import {categories} from './categories';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CategoryServiceService {
  categories = categories;
  constructor() { }
  getCategory(): Observable<any[]> {
    return of(this.categories);
  }
}
