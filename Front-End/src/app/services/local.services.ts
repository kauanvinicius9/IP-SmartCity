import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Local } from '../models/local';
import {environment} from '../../environments/environments';


@Injectable({
  providedIn: 'root'
})

export class LocalService {
  private http = inject(HttpClient);
  private base = environment.apiBase;
  
  listar():Observable<Local[]> {
    const url = `${this.base}api/local/`;
    return this.http.get<Local[]>(url);

  }
}