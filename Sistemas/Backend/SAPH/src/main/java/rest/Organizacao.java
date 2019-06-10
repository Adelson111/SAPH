/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package rest;

import Dao.OrganizacaoDao;
import com.google.gson.Gson;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

/**
 *
 * @author adelson
 */
@Path("organizacao")
public class Organizacao {
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public String get() {
        return "Eu sou Organizacao";
    }
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public String cadastrar(String organizacao) {
        new OrganizacaoDao().salvar(new Gson().fromJson(organizacao, modelo.Organizacao.class));
        return "Eu sou Organizacao";
    }
}
