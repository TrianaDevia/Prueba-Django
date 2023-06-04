import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tienda } from '../Tienda';

@Injectable({
  providedIn: 'root'
})
export class TiendaServiceService {
  private url = 'http://localhost:3000/producto';

  constructor(private http:HttpClient) { }

  public getTienda(): Observable<Tienda[]> {
    return this.http.get<Tienda[]>(this.url);
  }
}
