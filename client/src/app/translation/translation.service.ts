import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Translation } from '../model/translation';
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root',
})
export class TranslationService {

  private url: string = 'http://localhost:8001/translations/';

  constructor(
    private http: HttpClient
  ) { }

  addTranslation (translation: Translation): Observable<Translation> {
    return this.http.post<Translation>(this.url, translation, httpOptions);
  }
}
