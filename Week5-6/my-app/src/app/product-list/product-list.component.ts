import {Component, OnInit} from '@angular/core';
// import {categories} from '../categories';
import { ActivatedRoute } from '@angular/router';
import {ProductService} from '../product.service';
import {CategoryServiceService} from '../category-service.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products: any[];
  categoryType;
  categories;
  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private categoryService: CategoryServiceService,
  ) {}
  ngOnInit(): void {
    this.getProducts();
    this.getCategory();
    this.route.paramMap.subscribe(params => {
      this.categoryType = this.categories[+params.get('categoryId')];
    });
  }
  getProducts() {
    const observableProducts = this.productService.getProducts();
    observableProducts.subscribe(item => this.products = item);
  }
  getCategory() {
    const observableCategories = this.categoryService.getCategory();
    observableCategories.subscribe(categories => this.categories = categories);
  }
  share() {
    window.alert('The product has been shared!');
  }
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/
