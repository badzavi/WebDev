import { Component, OnInit } from '@angular/core';
import {CategoryServiceService} from '../category-service.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  categories: any[];
  constructor(private service: CategoryServiceService) { }

  ngOnInit(): void {
    this.getCategories();
  }
  getCategories() {
    const observableCategories = this.service.getCategory();
    observableCategories.subscribe(categories => this.categories = categories);
  }
}
