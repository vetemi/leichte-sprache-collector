import { Component } from '@angular/core';
import { Translation } from '../model/translation';
import { TranslationService } from './translation.service';

@Component({
  selector: 'translation',
  templateUrl: './translation.component.html'
})
export class TranslationComponent {
  translation: Translation = new Translation();

  constructor(
    private translationService: TranslationService
  ) {}

  public add() {
    this.translationService
      .addTranslation(this.translation)
      .subscribe(() => {
        this.translation.text = '';
        this.translation.translation = '';
      })
  }
}
