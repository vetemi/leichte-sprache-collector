import { Component } from '@angular/core';
import { Translation } from 'src/model/translation';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Hallo';
  translation: Translation
}
